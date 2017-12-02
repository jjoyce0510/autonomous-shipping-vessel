import cv2

class ObjectDetector:
	lidar = None

	Lower = (20, 80, 5)
	Upper = (80, 255, 185)

	ball_x = None
	ball_y = None
	ball_radius = None

	detectedObject = None

	def __init__(self, lidar=None):
		self.lidar = lidar
        

	def detectObject(self, frame):

		vertical_img = cv2.flip(frame, 1)
		# blur frame using Gaussian blur
		blurred_frame = cv2.GaussianBlur(vertical_img, (11, 11), 0)

		# conver the BGR image to HSV space
		hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

		# construct a mask for the color green, perform a series of dilations and erosions
		# to remove any small blobs left in the image
		mask = cv2.inRange(hsv, self.Lower, self.Upper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)

		# find the contours in the mask and initialize the current (x, y) center of the ball
		contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

		# only proceed if there are more than one contours
		if len(contours)>0:
			# find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
			c = max(contours, key=cv2.contourArea)
			# x, y, and radius can be accessed in order to determine how to navigate around objects
			((self.ball_x, self.ball_y), self.ball_radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

			# only proceed if radius is big enough to avoid error
			if self.ball_radius > 10:
				# draw the circle and centroid on the frame
				cv2.circle(frame, (int(self.ball_x), int(self.ball_y)), int(self.ball_radius), (0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)
				self.detectObjectWithCenter(center, self.ball_radius)

		else:
			self.ball_x = None
			self.ball_y = None
			self.ball_radius = None

		# Decide what to do here.
		# If object is detected, check the lidar.

		return frame

	def detectObjectWithCenter(self, center, radius):
		# Check the lidar, create a profile for the object, if it has lidar, we can put distance on it.
		# Set as global variable and allow the driver to request if there are any objects.
		pass

	def getObject(self):
		return self.detectedObject

