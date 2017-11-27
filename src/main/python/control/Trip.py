from src.main.python.exceptions.TripException import TripException
from TripState import TripState
import time

class Trip:
    startTime = None
    state = TripState.pending
    destinationCoordinates = None
    gps = None

    def __init__(self, gps):
        self.gps = gps

    def setDestinationCoordinates(self, destinationCoordinates):
        self.destinationCoordinates = destinationCoordinates

    def calculateDistanceToDestination(self, currentCoordinates):
        return self.destinationCoordinates.calculateDistanceTo(currentCoordinates)

    def calculateAngleToDestination(self, currentCoordinates, currentOrientation):
        # Calculate the relative angle to get to the coordinates - determine if we need to go right or left
        # Direction that we need to travel
        angleToDestination = self.currentCoordinates.calculateAngleTo(destinationCoordinates)
        # Adjustment that needs to be made
        #     (+) is clockwise rotation
        #     (-) is counter-clockwise rotation
        rotation = angleToDestination - currentOrientation
        # make rotation in shortest direction
        if rotation > 180:
        	rotation = rotation - 360
        if rotation < -180:
        	rotation = 360 - rotation
        return rotation

    def getDuration(self):
        if self.startTime is not None:
            return time.clock() - self.startTime
        else:
            return 0

    def getState(self):
        return self.state

    def startTrip(self):
        if self.destinationCoordinates is not None:
            self.state = TripState.active
            self.startTime = time.clock()
        else:
            raise TripException("Destination coordinates are undefined.")

    def completeTrip(self):
        if self.state is TripState.active:
            self.state = TripState.complete
            self.duration = time.clock() - self.startTime
        else:
            raise TripException("The trip has not begun yet.")


    def failTrip(self):
        if self.state is TripState.active:
            self.state = TripState.failed
            self.duration = time.clock() - self.startTime
        else:
            raise TripException("The trip has not begun yet")

    def reset(self):
        startTime = None
        state = TripState.pending
        destinationCoordinates = None