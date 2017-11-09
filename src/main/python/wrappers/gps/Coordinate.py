
# Created by Will Markley on November 8, 2017
class Coordinate:

	def __init__(self):
	   self.lat  = 0
	   self.long = 0
	
	def getLat(self):
		return self.lat
	
	def getLong(self):
		return self.long
	
	def setLat(self, latitude):
		self.lat  = latitude
	
	def setLong(self, longitude):
		self.long = longitude

