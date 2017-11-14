'''
TODO:
	import GPS device
	figure out how to get gps.lat, gps.long. gps.heading after importing
'''

###########

from Coordinates import Coordinates

# Created by Will Markley on November 8, 2017
class GPS:

	def __init__(self):
	   self.coord    = Coordinates()
	
	def getCoord(self):
		self.coord.setLat(gps.lat)
		self.coord.setLong(gps.long)
		return self.coord

	def getHeading(self):
		return gps.heading

