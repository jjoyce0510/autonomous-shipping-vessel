from ..TripState import TripState
import time
from TurningState import TurningState

STOP_DIST = 0.000009

# Singleton class to represent the driver, who is able to check the sensors and make decisions. USE GETINSTANCE
class VesselDriver:
    trip = None
    objectDetector = None # Should return an object, having distance and width that we can use to decide.
    vesselControls = None

    turningState = TurningState.NOT_TURNING

    def __init__(self, objectDetector, vesselControls):
        self.objectDetector = objectDetector
        self.vesselControls = vesselControls

    def setTrip(self, trip):
        if trip:
            self.trip = trip

    def getClosestObject(self):
        # Find and get closest obstacle
        return self.objectDetector.detectObject()

    # Probably want to multi thread here.
    def drive(self):
        # Drive the ship!, check for trip status, etc.
        # 1. Calculate, check for objects, determine direction to move
        # 2. Tell controllers how to move that way
        # 3. We're moving!
        if self.trip is not None and self.trip.getState() is TripState.pending:
            # Start drive loop
            self.trip.startTrip()
            self.beginMonitoring()

    def beginMonitoring(self):
        while self.trip.getState() is TripState.active:
            obj = self.getClosestObject()
            if obj.isValid():
                self.avoidObject(obj)
            else:
                # Move in direction toward completion of trip
                self.vesselControls.setAngle(30*self.trip.rotationToDestination()/180)
                trip_dist = self.trip.distanceToDestination()
                print " Trip dist " + str(trip_dist)
                if abs(trip_dist) < STOP_DIST:
                	self.vesselControls.setVelocity(0.0)
                else:
                	self.vesselControls.setVelocity(30.0)

            # Run every .2 seconds.
            time.sleep(0.2)

    def avoidObject(self, object):
        print "Angle from center = " + str(object.getAngleFromCenter())
        print "Distance from vessel = " + str(object.getDistance())





