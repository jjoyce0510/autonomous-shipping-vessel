from src.main.python.wrappers.camera.CameraStream import CameraStream
from src.main.python.wrappers.lidar.Lidar import Lidar
from src.main.python.control.ObjectDetector import ObjectDetector
from SingletonFactory import SingletonFactory

class ObjectDetectorFactory(SingletonFactory):
    def getInstance(self):
        return ObjectDetector(CameraStream(), Lidar())
