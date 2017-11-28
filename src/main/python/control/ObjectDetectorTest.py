from ObjectDetector import ObjectDetector
import time

myCamera = CameraController()
time.sleep(1)

myObjectDetector = ObjectDetector(myCamera, None)

myCamera.start()

myObjectDetector.detectObjectAndDisplay()