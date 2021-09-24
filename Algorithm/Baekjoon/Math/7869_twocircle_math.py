import math
import sys

def theta(R, r, d):
    return 2 * math.acos((pow(d, 2) + pow(R, 2) - pow(r, 2)) / (2 * d * R))

x1, y1, R, x2, y2, r = map(float, sys.stdin.readline().strip().split())
d: float = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
result: float = 0

if d + r <= R or d + R <= r:
    result = (min(R, r) ** 2) * math.pi
elif d >= R + r:
    result = 0.000
else:
    t1: float = theta(R, r, d)
    t2: float = theta(r, R, d)
    result: float = (pow(R, 2) * (t1 - math.sin(t1)) + pow(r, 2) * (t2 - math.sin(t2))) / 2

result = round(result, 3)

print("{:.3f}".format(result))