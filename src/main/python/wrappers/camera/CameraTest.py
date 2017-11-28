from CameraStream import CameraStream
import time


myCameraStream = CameraStream()
time.sleep(1)

myCameraStream.start()
time.sleep(1)

myCameraStream.display()

myCameraStream.stop()