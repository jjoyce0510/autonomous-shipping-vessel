from ..TripState import TripState
import time
import math
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

    def drive(self):
        if self.trip is not None and self.trip.getState() is TripState.pending:
            # Start drive loop
            self.trip.startTrip()
            self.vesselControls.startMotor()
            self.vesselControls.setVelocity(30.0)
            self.beginMonitoring()

    def beginMonitoring(self):
        while self.trip.getState() is TripState.active:
            obj = self.getClosestObject()
            if obj.isValid():
                self.avoidObject(obj)
            else:
                current_heading = self.trip.gps.getHeading()
                print "Current heading: " + str(current_heading)
                print "Rotation to dest: " + str(self.trip.rotationToDestination())
                # Move in direction toward completion of trip
                self.vesselControls.setAngle(self.vesselControls.servo.MAX_ANGLE_VALUE*self.trip.rotationToDestination()/180)
                trip_dist = self.trip.distanceToDestination()
                print " Trip dist " + str(trip_dist)

                if abs(trip_dist) < STOP_DIST:
                    self.vesselControls.setVelocity(0.0)
                    print "Arrived at destination."
                else:
                    self.vesselControls.setVelocity(30.0)

            # Run every .2 seconds.
            time.sleep(0.2)

    def avoidObject(self, object):
        print "Angle from center = " + str(object.getAngleFromCenter())
        print "Distance from vessel = " + str(object.getDistance())

        if object.getAngleFromCenter() is not None:
            self.vesselControls.setAngle(self.turningState * self.calculateTurnAngle(object))
        else:
            # Only lidar reading
            self.vesselControls.setVelocity(30.0)
            self.vesselControls.setAngle(self.vesselControls.servo.MAX_ANGLE_VALUE)

    def calculateTurnAngle(self, object):
        angle = object.getAngleFromCenter()
        radius = object.getRadiusProportion()
        print "Radius Proportion of screen" + str(radius)

        self.turningState = TurningState.TURNING_LEFT if (angle > 0) else TurningState.TURNING_RIGHT
        return self.mapRadiusToServoAngle(radius)



    def mapRadiusToServoAngle(self, radius):
        scaledRadius = 1 if radius > 0.50 else radius * 2
        return math.sqrt(scaledRadius) * self.vesselControls.servo.MAX_ANGLE_VALUE





