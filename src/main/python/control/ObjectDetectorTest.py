from src.main.python.control.ObjectDetector import ObjectDetector
from src.main.python.wrappers.camera.Camera import CameraController
import time

myCamera = CameraController(objectDetector=ObjectDetector(None))

time.sleep(1)
myCamera.start()
