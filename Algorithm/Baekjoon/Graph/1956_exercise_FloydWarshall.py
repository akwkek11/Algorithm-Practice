import copy
import sys

# Floyd Warshall (V^3)
def Floyd_Warshall(array: list) -> list:
    cost: list = copy.deepcopy(array)
    for k in range(len(array)):
        cost[k][k] = 0
        for i in range(len(array)):
            for j in range(len(array)):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
    
    for k in range(len(array)):
        cost[k][k] = float('inf')
        for i in range(len(array)):
            cost[i][i] = min(cost[i][i], cost[i][k]+cost[k][i])

    return cost

N, M = map(int, sys.stdin.readline().strip().split())
road_map: list = [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(M):
    i, j, road_cost = map(int, sys.stdin.readline().strip().split())
    road_map[i - 1][j - 1] = min(road_map[i - 1][j - 1], road_cost)

result: list = Floyd_Warshall(road_map)
min_cost: int = float('inf')

for i in range(len(result)):
    min_cost = min(min_cost, result[i][i])

print(f'{min_cost}') if min_cost != float('inf') else print('-1')