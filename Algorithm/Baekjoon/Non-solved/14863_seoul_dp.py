
import sys

n, k = map(int, sys.stdin.readline().strip().split())
road_map: list = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    walk_min, walk_cost, cycle_min, cycle_cost = map(int, sys.stdin.readline().strip().split())
    if i == 1:
        if walk_min <= k:
            road_map[1][walk_min] = walk_cost
        if cycle_min <= k:
            road_map[1][cycle_min] = cycle_cost
    
    else:
        for j in range(k + 1):
            if road_map[i - 1][j]:
                if j + walk_min <= k:
                    road_map[i][j + walk_min] = max(road_map[i][j + walk_min], road_map[i - 1][j] + walk_cost)
                if j + cycle_min <= k:
                    road_map[i][j + cycle_min] = max(road_map[i][j + cycle_min], road_map[i - 1][j] + cycle_cost)

print(max(road_map[n]))
