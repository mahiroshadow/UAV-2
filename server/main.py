import cv2
import time
import torch
import warnings
warnings.filterwarnings("ignore")
import subprocess
from queue import Queue
from flask import Flask, request
from flask_cors import CORS
from concurrent.futures import ThreadPoolExecutor
from utils import config_init, model_loader, FrameReadLoop
# from model.CSRNet import CSRNet


thread_pool = []
app = Flask(__name__)
CORS(app)

@app.route("/nuist/change",methods=["POST"])
def change_video():
    req = request.json
    pth, device, uid = req["pth"], req["device"], req["uid"]
    for t in thread_pool:
        t.running = False
    # thread_pool.clear()
    command = config["ffmpeg"]["command"]
    command[-1] = f"rtmp://121.43.36.206:6002/live/{uid}"
    processor = FrameReadLoop(pth,model,device,config["ffmpeg"]["command"])
    processor.start()
    thread_pool.append(processor)
    # processor.join()
    res = {"code":200,"data":"别问啥也没有"}
    return res 

@app.route("/nuist/test",methods=["POST"])
def test():
    res = {"code":200,"data":"别问啥也没有"}
    return res


if __name__ == "__main__":
    global config, model
    config = config_init("config.yml")
    model = model_loader(config)
    app.run(host="0.0.0.0",port=8888,debug=False)
