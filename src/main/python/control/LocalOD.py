import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

#lower = (30, 80, 5)
#upper = (40, 255, 185)
lower = (20, 80, 5)
upper = (80, 255, 185)

while(True):
	ret, frame = cap.read()

	blurred_frame = cv2.GaussianBlur(frame, (11, 11), 0)

	hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower, upper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None

	# only proceed if there are more than one contours
	if len(contours)>0:
		# find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
		c = max(contours, key=cv2.contourArea)
		((ball_x, ball_y), ball_radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if radius is big enough to avoid error
		if ball_radius > 10:
			# draw the circle and centroid on the frame
			cv2.circle(frame, (int(ball_x), int(ball_y)), int(ball_radius), (0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)

	cv2.imshow("Frame w/ Object Detection", cv2.flip(frame, 1))

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()



