import cv2
from Object import Object

class ObjectDetector:
	lidar = None
	detectedObject = Object() # Update this object

	def __init__(self, camera=None, lidar=None, imageProc=None):
		self.lidar = lidar
		self.camera = camera
		self.imageProc = imageProc

	def detectObject(self):
		distanceToNearestObject = self.lidar.getDistance()
		# If at any moment the distance to the nearest obj is less than a certain amount, go for it.

		# Prioritize the camera stream. Distance, unless extremely close, doesn't matter too much.
		# When no camera object detected, use the lidar.

		# If we already have an obj, means the camera is on.
		if self.camera.isActive is False:
			self.camera.start()
		# Camera is active. Can use fields of object from Camera.
		else:
			# This means that there is object detected on the camera.
			if self.imageProc.hasDetectedObjectInImage():
				self.detectedObject.setAngleFromCenter(self.imageProc.getObjectAngleFromCenter())
				self.detectedObject.setDiameterProportion(self.imageProc.getDiameterAsProportionOfCameraView())

				proportionOfView = self.detectedObject.getDiameterProportion()

				# Determine if the distance is representative.
				if abs(self.detectedObject.getAngleFromCenter()) > self.imageProc.getHorizFieldOfView() * proportionOfView:
					# We don't think its presentation.
					self.detectedObject.setDistance(None)
				else:
					# Center
					self.detectedObject.setDistance(distanceToNearestObject)

			# Nothing detected on camera, must resort to lidar.
			else:
				if distanceToNearestObject < 200:
					# Object less than a meter, no object detected on camera.
					self.detectedObject.setDistance(distanceToNearestObject)
				else:
					self.detectedObject.setDistance(None)

				self.detectedObject.setAngleFromCenter(None)
				self.detectedObject.setDiameterProportion(None)

		return self.detectedObject

