
# Created by Will Markley on November 8, 2017
class Coordinates:

	def __init__(self, lat, long):
	   self.lat  = lat
	   self.long = long

	def getLat(self):
		return self.lat
	
	def getLong(self):
		return self.long
	
	def setLat(self, latitude):
		self.lat  = latitude
	
	def setLong(self, longitude):
		self.long = longitude

	def calculateDistanceTo(self, coordinates):
		# Calculate distance to another set of coordinates
		return 0


