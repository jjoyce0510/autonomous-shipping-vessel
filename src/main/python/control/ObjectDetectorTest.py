from src.main.python.control.ObjectDetector import ObjectDetector

myCamera = CameraController()
time.sleep(1)

myObjectDetector = ObjectDetector(myCamera, None)

myCamera.start()

myObjectDetector.detectObjectAndDisplay()
