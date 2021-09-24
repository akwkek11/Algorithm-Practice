from collections import defaultdict

import heapq
import sys

def dijkstra(graph: defaultdict, start: str) -> defaultdict:
    distances = defaultdict(lambda: float('inf'))
    for node in graph:
        distances[node]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance

            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    N, M, T = map(int, sys.stdin.readline().strip().split())
    S, G, H = map(int, sys.stdin.readline().strip().split())
    map_dict: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for _ in range(M):
        start, end, cost = map(int, sys.stdin.readline().strip().split())
        if map_dict[start][end] > cost:
            map_dict[start][end] = cost
            map_dict[end][start] = cost

    
    target_list: list = [int(sys.stdin.readline().strip()) for _ in range(T)]
    map1: dict = dijkstra(map_dict, S)
    map2: dict = dijkstra(map_dict, G)
    map3: dict = dijkstra(map_dict, H)

    res_list: list = []
    for i in target_list:
        target_distance: int = min(map1[G] + map2[H] + map3[i], map1[H] + map3[G] + map2[i])
        if target_distance < float('inf') and map1[i] >= target_distance:
            res_list.append((i, target_distance))

    res_list.sort(key=lambda x: x[0])
    for i in range(len(res_list)):
        print(f'{res_list[i][0]}', end=' ') if i != len(res_list) - 1 else print(f'{res_list[i][0]}')