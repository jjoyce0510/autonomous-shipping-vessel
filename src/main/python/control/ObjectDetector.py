class ObjectDetector:
    camera = None
    lidar = None

    def __init__(self, camera, lidar):
        self.camera = camera
        self.lidar = lidar


    #def detectObject(self):