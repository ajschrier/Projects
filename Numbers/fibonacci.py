import sys
import time

n = int(sys.argv[1])

series = [0, 1]

while len(series) < n:
    series.append(series[-1] + series[-2])

for i in range(0, len(series)):
    print series[i]
    time.sleep(0.2)
