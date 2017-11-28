from picamera.array import PiRGBArray
from picamera import PiCamera
from src.main.python.control.ObjectDetector import ObjectDetector
import time
import cv2

## Created by Anthony Daegele, Nov. 7 2017
class CameraController:

	def __init__(self, resolution=(320,240), framerate=32, objectDetector=None):
		self.camera = PiCamera()
		self.camera.resolution = resolution
		self.camera.framerate = framerate
		self.rawCapture = PiRGBArray(self.camera, resolution)
		# time for camera to warm up
		time.sleep(0.1)

		self.frame = None
		self.stopped = False
		self.detector = objectDetector



	def start(self):
		# start the thread and read frames from the video stream

		#Thread(target=self.update, args=()).start()
		self.update()


	def update(self):
		# loop until thread is stopped
		for f in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
			self.frame = f.array
			self.frame = self.detector.update(f.array)

			cv2.imshow("frame", self.frame)

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
