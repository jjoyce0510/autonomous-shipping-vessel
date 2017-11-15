from Camera import CameraController
import time
import cv2

class CameraStream:

	def __init__(self, resolution=(320,240), framerate=32):
		self.stream = CameraController()

	def start(self):
		return self.stream.start()

	def stop(self):
		return self.stream.stop()

	def display(self):
		end_time = time.time() + 10

		# loop through and display camera stream for 10 seconds
		while time.time() < end_time:
			# grab the current frame
			frame = self.stream.read()

			# show the current frame in window
			cv2.imshow("Frame", frame)

		cv2.destroyAllWindows()
		self.stop()
