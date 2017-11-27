from src.main.python.wrappers.camera.Camera import CameraController
from ObjectDetector import ObjectDetector
import time

myCamera = CameraController()
time.sleep(1)

myCamera,start()
time.sleep(1)

myObjectDetector = ObjectDetector(myCamera, None)

myObjectDetector.detectObjectAndDisplay()