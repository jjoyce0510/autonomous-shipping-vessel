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
		self.stream = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)
		# time for camera to warm up
		time.sleep(0.1)

		self.frame = None
		self.stopped = False
		self.object_detector = objectDetector



	def start(self):
		# start the thread and read frames from the video stream
		#Thread(target=self.update, args=()).start()
		self.update()


	def update(self):
		# loop until thread is stopped

		for f in self.stream:
			self.frame = self.object_detector.detectObject(f.array)

			# next few lines should be commented out when deploying boat, they are only for displaying frame
			################################################
			cv2.imshow("Frame w/ object detection", self.frame)
			self.rawCapture.truncate(0)
			# break and stop streaming if q is pressed
			if cv2.waitKey(1) & 0xFF == ord('q'):
				self.stop()
			################################################	

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
