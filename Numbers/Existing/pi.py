from math import atan
import sys

digits = sys.argv[1]

print ('{0:.%df}' % min(30,
                        int(digits))).format(
                        4 * (4 * atan(1.0/5.0) - atan(1.0/239.0)))
