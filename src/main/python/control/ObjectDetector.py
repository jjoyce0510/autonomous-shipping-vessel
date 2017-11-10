from src.main.python.factories.ObjectDetectorFactory import ObjectDetectorFactory
class ObjectDetector:
    gps = None
    lidar = None

    def __init__(self, gps, lidar):
        self.gps = gps
        self.lidar = lidar


    #def detectObject(self):