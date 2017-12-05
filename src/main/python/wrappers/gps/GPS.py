
import gps
from Coordinates import Coordinates

PORT = 2947

# Created by Will Markley on November 8, 2017
# Sources:
#     https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi?view=all
#     http://www.catb.org/gpsd//gpsd_json.html
class GPS:

	def __init__(self):
		self.coord     = Coordinates(0,0)
		self.gpsd      = gps.gps("localhost", PORT)
		self.gpsd.stream (gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
	
	def getCoord(self):
		for report in self.gpsd:
			if report['class'] == 'TPV':
				if hasattr(report, 'lat'):
					self.coord.setLat(report['lat'])
				if hasattr(report, 'lon'):
					self.coord.setLon(report['lon'])
				return self.coord

	def getHeading(self):
		for report in self.gpsd:
			if report['class'] == 'TPV':
				if hasattr(report, 'track'):
					return report.track
				else:
					return ""


	def getSpeed(self):
		for report in self.gpsd:
			if report['class'] == 'TPV':
				if hasattr(report, 'speed'):
					return report.speed * gps.MPS_TO_KPH
				else:
					return ""