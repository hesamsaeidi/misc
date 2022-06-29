import sys
from numpy import arctan, tan, radians, degrees

def geoc2geod(gclat, colat_out = True):
    # the input should be geocentric colatitude
    # the output will be geodetic colatitude unless
    # colat_out was given False
    gclat = 90 - float(gclat)

    f = 0.00335281066474748071984552861852 # Earth Flattening Factor (WGS-84)
    f_const = 1/(1-f)**2
    gdlat = arctan(f_const*tan(radians(gclat)))
    if colat_out:
        return 90-degrees(gdlat)
    else:
        return degrees(gdlat)
