from CameraStream import CameraStream
import time


myCameraStream = CameraStream()
time.sleep(1)

myCameraStream.start()

myCameraStream.display()

myCameraStream.stop()