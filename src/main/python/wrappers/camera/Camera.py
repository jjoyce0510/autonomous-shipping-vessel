from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread 
import time
import cv2

## Created by Anthony Daegele, Nov. 7 2017
class CameraController:

	def __init__(self, resolution=(320,240), framerate=32):
		self.camera = PiCamera()
		self.camera.resolution = resolution
		self.camera.framerate = framerate
		self.rawCapture = PiRGBArray(self.camera, resolution)
		# time for camera to warm up
		time.sleep(0.1)
		self.stream = self.camera.capture_continuous(self.rawCapture, format="brg", use_video_port=True)

		self.frame = None
		self.stopped = False

	def start(self):
		# start the thread and read frames from the video stream
		Thread(target=self.update, args=()).start()

	def update(self):
		# loop until thread is stopped
		for f in self.stream:
			self.frame = f.array
			self.rawCapture.truncate(0)

			if self.stopped:
				self.stream.close()
				self.rawCapture.close()
				self.camera.close()
				return

	def read(self):
		# return the most recent frame
		return self.frame

	def stop(self):
		# stop the thread
		self.stopped = True
