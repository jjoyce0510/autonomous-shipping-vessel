from src.main.python.wrappers.camera.CameraStream import CameraStream
from src.main.python.wrappers.lidar.Lidar import Lidar
from src.main.python.control.ObjectDetector import ObjectDetector
from src.main.python.control.ImageProcessor import ImageProcessor
from SingletonFactory import SingletonFactory

class ObjectDetectorFactory(SingletonFactory):
    def getInstance(self):
        imgProcessor = ImageProcessor()
        return ObjectDetector(CameraStream(imgProcessor), Lidar(), imgProcessor)
