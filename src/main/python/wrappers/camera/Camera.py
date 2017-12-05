from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread
import time
import cv2

## Created by Anthony Daegele, Nov. 7 2017
class CameraController:

	def __init__(self, resolution=(640,480), framerate=24, imageProcessor=None):
		self.camera = PiCamera()
		self.camera.resolution = resolution
		self.camera.framerate = framerate
		self.rawCapture = PiRGBArray(self.camera, resolution)
		time.sleep(0.1)

		self.responseAction = None
		self.stream = None
		self.frame = None
		self.isActive = False
		self.imageProcessor = imageProcessor


	def start(self):
		# start the thread and read frames from the video stream
		self.isActive = True
		Thread(target=self.update).start()


	def update(self):
		# loop until thread is stopped

		for f in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
			self.frame = self.imageProcessor.detectObjectInFrame(f.array)

			# next few lines should be commented out when deploying boat, they are only for displaying frame
			################################################
			cv2.imshow("Frame w/ object detection", self.frame)
			self.rawCapture.truncate(0)
			# break and stop streaming if q is pressed
			if cv2.waitKey(1) & 0xFF == ord('q'):
				self.stop()
			################################################	

			if not self.isActive:
				self.rawCapture.close()
				#self.camera.close()
				return

	def stop(self):
		# stop the thread
		self.isActive = False

	def isActive(self):
		return self.isActive
