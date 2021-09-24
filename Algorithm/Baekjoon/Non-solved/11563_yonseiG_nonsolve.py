# Not Solved

import sys

n, m = map(int, sys.stdin.readline().strip().split())
y_map: list = []
k_map: list = []
minimum_length: float = 1000000000.0

def dist(P, A, B):
    area = abs ((A[0] - P[0]) * (B[1] - P[1]) - (A[1] - P[1]) * (B[0] - P[0]))
    AB = ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
    return area / AB

for _ in range (n):
    xs, ys, xe, ye = map(float, sys.stdin.readline().strip().split())
    y_map.append((xs, ys))
    y_map.append((xe, ye))

for _ in range (m):
    xs, ys, xe, ye = map(float, sys.stdin.readline().strip().split())
    k_map.append((xs, ys))
    k_map.append((xe, ye))

temp_length: float = 0
for i in range(n):
    for j in range(0, m, 2):
        temp_length = dist(y_map[i], k_map[j], k_map[j+1])
        minimum_length = temp_length if temp_length < minimum_length else minimum_length
        
print(f'{minimum_length}')