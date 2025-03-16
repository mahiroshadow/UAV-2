import cv2
import torch
import warnings

warnings.filterwarnings("ignore")
import subprocess
from queue import Queue
from flask import Flask, request
from utils import config_init, model_loader, FrameReadLoop

app = Flask(__name__)


@app.route("/nuist/change", methods=["POST"])
def change_video():
    req = request.json
    pth, device = req["pth"], req["device"]
    processor = FrameReadLoop(pth, model, device, config["ffmpeg"]["command"])
    processor.start()
    processor.join()
    res = {"code": 200}
    return res


@app.route("/nuist/test", methods=["POST"])
def test():
    res = {"code": 200}
    return res


if __name__ == "__main__":
    global config, model
    config = config_init("config.yml")
    model = model_loader(config)
    app.run(host="0.0.0.0", port=8888, debug=False)
