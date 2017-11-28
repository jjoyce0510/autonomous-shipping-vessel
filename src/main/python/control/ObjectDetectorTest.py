from src.main.python.control.ObjectDetector import ObjectDetector
from src.main.python.wrappers.camera.Camera import CameraController
import time

myCamera = CameraController()
time.sleep(1)

myObjectDetector = ObjectDetector(myCamera, None)

myCamera.start()

myObjectDetector.detectObjectAndDisplay()
