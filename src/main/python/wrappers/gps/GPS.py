
import gps
from Coordinates import Coordinates

PORT = 2947

# Created by Will Markley on November 8, 2017
class GPS:

	def __init__(self):
		self.coord     = Coordinates(0,0)
		self.gpsd      = gps.gps("localhost", PORT)
		self.gpsd.stream (gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
	
	def getCoord(self):
		for report in gpsd:
			if report['class'] == 'TPV':
				self.coord.setLat(report['lat'])
				self.coord.setLon(report['lon'])
				return self.coord

	def getHeading(self):
		for report in gpsd:
			if report['class'] == 'TPV':
				return report['track']
