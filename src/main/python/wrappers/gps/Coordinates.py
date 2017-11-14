
# Created by Will Markley on November 8, 2017
class Coordinates:

	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon

	def getLat(self):
		return self.lat
	
	def getLon(self):
		return self.lon
	
	def setLat(self, latitude):
		self.lat  = latitude
	
	def setLon(self, longitude):
		self.lon = longitude

	def calculateDistanceTo(self, coordinates):
		# Calculate distance to another set of coordinates
		return math.sqrt( math.pow((self.lat - coordinates.getLat()),2) + math.pow((self.lon - coordinates.getLon()),2) )
