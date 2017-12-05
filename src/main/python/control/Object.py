
# Object class used to help the driver determine where to go.
class Object:
    distanceInCm = None
    radProp = 0.0
    angleFromCenter = 0.0

    # This probably not always reliable, unless we are going straight into something.
    def getDistance(self):
        return self.distanceInCm

    def setDistance(self, dist):
        self.distanceInCm = dist

    def setRadiusProportion(self, radProp):
        self.radProp = radProp

    def setAngleFromCenter(self, angleFromCenter):
        self.angleFromCenter = angleFromCenter

    def getAngleFromCenter(self):
        return self.angleFromCenter

    def getRadiusProportion(self):
        return self.radProp

    def isValid(self):
        return self.distanceInCm is not None or self.radProp is not None or self.angleFromCenter is not None