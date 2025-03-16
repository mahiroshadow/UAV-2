import cv2
import yaml
import time
import torch
import subprocess
from queue import Queue
from threading import Thread
from model.CSRNet import CSRNet
from torchvision import transforms
from scipy.ndimage import gaussian_filter

def config_init(pth):
    file = open(pth,"r",encoding="utf-8")
    config = yaml.load(file.read(), Loader=yaml.FullLoader)
    config["ffmpeg"]["command"] = command = [
        'ffmpeg', '-y', '-f', 'rawvideo', '-vcodec', 'rawvideo', '-pix_fmt',
        'bgr24', '-s', "{}x{}".format(1280, 720), '-r',
        str(config["ffmpeg"]["fps"]), '-i', '-', '-c:v', 'libx264', '-b:v', '2500k', '-pix_fmt',
        'yuv420p', '-preset', 'ultrafast', '-f', 'flv', config["rtmp"]["to"]
    ]   
    return config

def model_loader(config):
    net = CSRNet().to(config["model"]["device"])
    info = torch.load(config["model"]["save"], map_location=config["model"]["device"], weights_only=True)
    net.load_state_dict(info['state_dict'])
    return net

def _count_crowd_image(img,net,device,raw=False, only=False, nofont=False):
    with torch.no_grad():
        temp = img.copy()
        img = transforms.ToTensor()(img)
        img = transforms.Normalize(mean=(img[0].mean(), img[1].mean(), img[2].mean()),
                                   std=(img[0].std(), img[1].std(), img[2].std()))(img).unsqueeze(0).to(device)
        output = net(img)
        n = int(output.sum() + 0.5)
        output = output[0, 0]
        if raw:
            return n, (output * 255).cpu().numpy()
        output = torch.Tensor(gaussian_filter(output.cpu(), 1))
        output = (output - output.min()) / (output.max() - output.min())
        h = 240 * (1 - output)
        s = torch.zero_(output) + 1
        v = torch.zero_(output) + 180
        output = torch.stack((h, s, v), dim=0)
        output = cv2.cvtColor(output.numpy().transpose(1, 2, 0), cv2.COLOR_HSV2BGR)
        output = cv2.resize(output, (img.shape[3], img.shape[2]), interpolation=cv2.INTER_LINEAR)
        if only:
            return n, output
        output = cv2.addWeighted(temp, 0.7, output, 0.9, 0, dtype=cv2.CV_8U)
        if nofont:
            return n, output
        cv2.putText(output, f'Count: {n}', (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (30, 30, 30), 2)
    return n, output


def video_estimate(pth,net,device,alive=False,command=[],save_pth=""):
    cap = cv2.VideoCapture(pth)
    if alive:
        pipe = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE)
        writer = pipe.stdin
    else:
        writer = cv2.VideoWriter(save_pth, cv2.VideoWriter_fourcc(*'mp4v'),
                             video.get(cv2.CAP_PROP_FPS), (int(video.get(3)), int(video.get(4))))
    while True:
        _, frame = cap.read()
        n, res_frame = _count_crowd_image(frame,net,device)
        writer.write(res_frame)
    if not alvie:
        writer.release()

class FrameReadLoop(Thread):
    def __init__(self,pth,net,device,command):
        super(FrameReadLoop, self).__init__()
        self.pth = pth
        self.net = net
        self.device = device
        self.pipe = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE)
 
    def run(self):
        cap = cv2.VideoCapture(self.pth)
        while True:
            _, frame = cap.read()
            n, res_frame = _count_crowd_image(frame,self.net,self.device)
            # self.queue.put(res_frame)
            self.pipe.stdin.write(res_frame)
'''
class PushFrameLoop(Thread):
    def __init__(self, command, queue):
        super(PushFrameLoop, self).__init__()
        self.pipe = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty()!= True:
                frame = self.queue.get()
                self.pipe.stdin.write(frame)
'''










