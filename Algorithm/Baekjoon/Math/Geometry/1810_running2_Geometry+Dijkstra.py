from collections import defaultdict

import heapq
import sys

def dijkstra(graph: defaultdict, start: tuple, end: int) -> float:
    distances: defaultdict = defaultdict(lambda: float('inf'))
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if end == current_destination[1]:
            return current_distance

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance

            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return float('inf')

N, F = map(int, sys.stdin.readline().strip().split())
map_dict: defaultdict = defaultdict(list)
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    for i in range((x - 2), (x + 2) + 1):
        for j in range((y - 2), min(F, (y + 2)) + 1):
            map_dict[(i, j)].append([(x, y), ((x - i) ** 2 + (y - j) ** 2) ** 0.5])

res_length: float = dijkstra(map_dict, (0, 0), F)
print(f'{int(round(res_length, 0))}') if res_length != float('inf') else print('-1')