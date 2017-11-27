
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

	def calculateAngleFrom(self, coordinates):
		# Calculate angle from self to another set of coordinates
		# Angle represented as degrees from true north
		'''
		Longitude: East (+), West (-) from GPS
		Latitude:  North (+), South (-) from GPS
		
		         E
			     |
			S <--+--> N
		         |
		         W
				 
		Y-axis is longitude
		X-axis is latitude
			
		'''
		latDifference = coordinates.getLat() - self.lat
		lonDifference = coordinates.getLon() - self.lon
		# atan2 returns the correct quadrant and accounts for directly East and directly West
		return math.degrees(math.atan2(lonDifference,latDifference))

