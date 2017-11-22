from GPS import GPS

gps = GPS()

coord = gps.getCoord()
print coord.getLat()
print coord.getLon()

print gps.getHeading()