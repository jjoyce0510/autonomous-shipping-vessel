from src.main.python.wrappers.gps import GPS
from src.main.python.wrappers.lidar.Lidar import Lidar
from src.main.python.control.ObjectDetector import ObjectDetector
from SingletonFactory import SingletonFactory

class ObjectDetectorFactory(SingletonFactory):
    def createInstance(self):
        return ObjectDetector(GPS(), Lidar())
