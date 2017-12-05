import math

# Created by Will Markley on November 8, 2017
class Coordinates:

	def __init__(self, lat, lon):
		self.lat = float(lat)
		self.lon = float(lon)

	def getLat(self):
		return self.lat
	
	def getLon(self):
		return self.lon
	
	def setLat(self, latitude):
		self.lat  = float(latitude)
	
	def setLon(self, longitude):
		self.lon = float(longitude)

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

	def calculateRotation(self, current, goal):
		# Calculate rotation in degrees from current angle to desired angle
		#     (+) is clockwise rotation
		#     (-) is counter-clockwise rotation
		
		## Reduce input angles to below 360 in value
		if abs(current) > 360:
			if current > 0:
				current = current % 360
			else:
				current = -1*(abs(current) % 360)
		if abs(goal) > 360:
			if goal > 0:
				goal = goal % 360
			else:
				goal = -1*(abs(goal) % 360)		
		
		## Calculate difference
		rotation = goal - current
		
		## Make rotation in shortest direction (smallest magnitude)
		if rotation > 180:
			rotation = rotation - 360
		elif rotation < -180:
			rotation = 360 + rotation
		
		## Check rotation is in shortest direction
		if abs(rotation) > 180:
			return "Error: rotation is "+str(rotation)
		
		return rotation
