from src.main.python.wrappers.camera.Camera import CameraController
from src.main.python.wrappers.lidar.Lidar import Lidar
from src.main.python.control.ObjectDetector import ObjectDetector
from src.main.python.control.ImageProcessor import ImageProcessor
from SingletonFactory import SingletonFactory

class ObjectDetectorFactory(SingletonFactory):
    def getInstance(self):
        imgProcessor = ImageProcessor()
        return ObjectDetector(CameraController(imageProcessor=imgProcessor), Lidar(), imgProcessor)
