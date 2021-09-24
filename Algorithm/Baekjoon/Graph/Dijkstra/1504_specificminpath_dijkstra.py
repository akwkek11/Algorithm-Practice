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

N, E = map(int, sys.stdin.readline().strip().split())
map_dict: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))

for i in range(1, N + 1):
    map_dict[i]
for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    if map_dict[start][end] > cost:
        map_dict[start][end] = cost
        map_dict[end][start] = cost

point1, point2 = map(int, sys.stdin.readline().strip().split())
map1: dict = dijkstra(map_dict, 1)
map2: dict = dijkstra(map_dict, point1)
map3: dict = dijkstra(map_dict, point2)

if map1[point1] != float('inf') and map1[point2] != float('inf') and map1[N] != float('inf'):
    print(f'{min(map1[point1] + map2[point2] + map3[N], map1[point2] + map3[point1] + map2[N])}')
else:
    print('-1')