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

    return cost

N: int = int(sys.stdin.readline().strip())
road_map: list = [[float('inf') for _ in range(N)] for _ in range(N)]
M: int = int(sys.stdin.readline().strip())
for _ in range(M):
    i, j, road_cost = map(int, sys.stdin.readline().strip().split())
    road_map[i - 1][j - 1] = min(road_map[i - 1][j - 1], road_cost)

res_map: list = Floyd_Warshall(road_map)
for i in range(N):
    for j in range(N):
        print_num: int = res_map[i][j]
        if res_map[i][j] == float('inf'):
            print_num = 0
        print(f'{print_num}', end=' ') if j < N - 1 else print(f'{print_num}')