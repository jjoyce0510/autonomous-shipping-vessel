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

    def calculateAngleToDestination(self, currentCoordinates):
        # Calculate the relative angle to get to the destination coordinates (Direction that we need to travel)
	return self.currentCoordinates.calculateAngleTo(destinationCoordinates)
        
    def calculateRotationToDestination(self, currentCoordinates, currentOrientation):
	# Calculate rotation in degrees of boat from current orientation to desired orientation
	#     (+) is clockwise rotation
	#     (-) is counter-clockwise rotation
	angleToDestination = self.currentCoordinates.calculateAngleTo(destinationCoordinates)
	return self.destinationCoordinates.calculateRotation(currentOrientation, angleToDestination)
        
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
