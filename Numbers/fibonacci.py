import sys
import time

try:
    n = int(sys.argv[1])
except IndexError:
    print "Defaulting to 10"
    n = 10

# if input > 0:
#     print "Defaulting to 10"
#     n = 10
# else:
#     n = int(input)

series = [0, 1]

while len(series) < n:
    series.append(series[-1] + series[-2])

for i in range(0, len(series)):
    print series[i]
    time.sleep(0.2)
