from src.main.python.wrappers.gps.Coordinates import Coordinates

# Created by Will Markley on November 27, 2017
class TestCoordinates:

	def __init__(self):
		self.coord_0 = Coordinates(0,0)
		self.coord_1 = Coordinates(1,2)
		self.coord_2 = Coordinates(0,0)
		self.coord_3 = Coordinates(4,6)
		self.coord_4 = Coordinates(1,1)
		self.coord_5 = Coordinates(-1,-1)
		self.coord_6 = Coordinates(1,-1)
		self.coord_7 = Coordinates(-1,1)
		self.coord_8 = Coordinates(0,1)
		self.coord_9 = Coordinates(1,0)
		self.coord_10 = Coordinates(-1,0)
		self.coord_11 = Coordinates(0,-1)
		self.coord_tests()

	def coord_tests(self):
		assert(self.test_getLat())
		assert(self.test_getLon())
		assert(self.test_setLat())
		assert(self.test_setLon())
		assert(self.test_calculateDistanceTo())
		assert(self.test_calculateAngleFrom())
		assert(self.test_calculateRotation())
		print "Coordinates Tests Completed"
	
	def test_getLat(self):
		if self.coord_0.getLat() != 0:
			return False
		if self.coord_1.getLat() != 1:
			return False
		return True
	
	def test_getLon(self):
		if self.coord_0.getLon() != 0:
			return False
		if self.coord_1.getLon() != 2:
			return False
		return True
		
	def test_setLat(self):
		if self.coord_2.getLat() != 0:
			return False
		self.coord_2.setLat(3)
		if self.coord_2.getLat() != 3:
			return False
		return True
	
	def test_setLon(self):
		if self.coord_2.getLon() != 0:
			return False
		self.coord_2.setLon(4)
		if self.coord_2.getLon() != 4:
			return False
		return True
		
	def test_calculateDistanceTo(self):
		if self.coord_1.calculateDistanceTo(self.coord_3) != 5.0:
			return False
		return True
	
	def test_calculateAngleFrom(self):
		out = self.coord_1.calculateAngleFrom(self.coord_3)
		if out < 53.1 or out > 53.2:
			return False
		if self.coord_0.calculateAngleFrom(self.coord_4) != 45:
			return False
		if self.coord_0.calculateAngleFrom(self.coord_5) != -135:
			return False
		if self.coord_0.calculateAngleFrom(self.coord_6) != -45:
			return False
		if self.coord_0.calculateAngleFrom(self.coord_7) != 135:
			return False
		if self.coord_0.calculateAngleFrom(self.coord_8) != 90:
			return False
		if self.coord_0.calculateAngleFrom(self.coord_9) != 0:
			return False
		if self.coord_0.calculateAngleFrom(self.coord_10) != 180:
			return False
		if self.coord_0.calculateAngleFrom(self.coord_11) != -90:
			return False
		return True
	
	def test_calculateRotation(self):
		if self.coord_0.calculateRotation(0, 45) != 45:
			return False
		if self.coord_0.calculateRotation(-45, 45) != 90:
			return False
		if self.coord_0.calculateRotation(-180, 45) != -135:
			return False
		if self.coord_0.calculateRotation(50, 45) != -5:
			return False
		if self.coord_0.calculateRotation(50, 90) != 40:
			return False
		if self.coord_0.calculateRotation(180, 190) != 10:
			return False
		if self.coord_0.calculateRotation(270, 0) != 90:
			return False
		if self.coord_0.calculateRotation(270, 89) != 179:
			return False
		if self.coord_0.calculateRotation(720, 1081) != 1:
			return False
		if self.coord_0.calculateRotation(0, 180) != 180:
			return False
		if self.coord_0.calculateRotation(180, 0) != -180:
			return False
		if self.coord_0.calculateRotation(315, -10) != 35:
			return False
		if self.coord_0.calculateRotation(315, 45) != 90:
			return False
		if self.coord_0.calculateRotation(315, -90) != -45:
			return False
		return True


