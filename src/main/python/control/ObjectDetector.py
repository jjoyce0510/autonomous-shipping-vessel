from src.main.python.factories.ObjectDetectorFactory import ObjectDetectorFactory
from src.main.python.wrappers.camera.CameraStream import CameraStream
from src.main.python.wrappers.camera.Camera import CameraController

class ObjectDetector:
    camera = None
    lidar = None

    greenLower = (29, 86, 6)
    greenUpper = (64, 255, 255)

    def __init__(self, camera, lidar=None):
        self.camera = camera
        self.lidar = lidar


    def detectObjectAndDisplay(self):

    	while True:
    		# grab the frame from the camera
    		frame = self.camera.read()

    		# blur frame using Gaussian blur
    		blurred_frame = cv2.GaussianBlur(frame, (11, 11), 0)

    		# conver the BGR image to HSV space
    		hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    		# construct a mask for the color green, perform a series of dilations and erosions
    		# to remove any small blobs left in the image
    		mask = cv2.inRange(hsv, self.greenLower, self.greenUpper)
    		mask = cv2.erode(mask, None, iterations=2)
    		mask = cv2.dilate(mask, None, iterations=2)

    		# find the contours in the mask and initialize the current (x, y) center of the ball
    		contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    		center = None

    		# only proceed if there are more than one contours
    		if len(contours)>0:
    			# find the largest contour in the mask, then use it to compute the minimum eclosing circle and centroid
    			c = max(contours, key=cv2.contourArea)
    			((x, y), radius) = cv2.minEclosingCircle(c)
    			M = cv2.moments(c)
    			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    			# only proceed if radius is big enough to avoid error
    			if radius > 10:
    				# draw the circle and centroid on the frame
    				cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
    				cv2.circle(frame, center, 5, (0, 0, 255), -1)

    		# display frames with circles around green ball
    		cv2.imshow("Frame", frame)
    		# display mask
    		cvs.imshow("Mask", mask)
    		key = cv2.waitkey(0) & 0xFF

    		if key == ord("q"):
    			break

    	cv2.destroyAllWindows()

