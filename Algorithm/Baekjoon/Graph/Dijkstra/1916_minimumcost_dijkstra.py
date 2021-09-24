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

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
map_dict: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    if map_dict[start][end] > cost:
        map_dict[start][end] = cost

start, end = map(int, sys.stdin.readline().strip().split())
print(f'{dijkstra(map_dict, start)[end]}')