from collections import defaultdict

import heapq
import sys

T: int = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().strip().split())
    map_dict: defaultdict = defaultdict(lambda : defaultdict(list))

    for i in range(1, N + 1):
        map_dict[i]

    for _ in range(K):
        start, end, sub_length, time = map(int, sys.stdin.readline().strip().split())
        map_dict[start][end].append((sub_length, time))
    
    distances: list = [[float('inf') for _ in range(M + 1)] for _ in range(N + 1)]
    distances[1][0] = 0
    
    for j in range(M + 1):
        for i in range(1, N + 1):
            if distances[i][j] == float('inf'):
                continue

            now_distance: int = distances[i][j]
            for target, target_information in map_dict[i].items():
                for target_length, target_distance in target_information:
                    if j + target_length > M:
                        continue

                    distances[target][j + target_length] = min(distances[target][j + target_length], now_distance + target_distance)

    min_cost: int = float('inf')
    for i in distances[N]:
        min_cost = min(min_cost, i)
    print(f'{min_cost}') if min_cost != float('inf') else print('Poor KCM')