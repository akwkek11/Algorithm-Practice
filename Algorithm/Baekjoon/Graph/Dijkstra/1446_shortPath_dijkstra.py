from collections import defaultdict

import heapq
import sys

def dijkstra(graph: defaultdict, start: str) -> dict:
    distances = {node: float('inf') for node in graph}
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

N, end = map(int, sys.stdin.readline().strip().split())
map_dict: defaultdict = defaultdict(dict)

for i in range(0, end):
    map_dict[i][i+1] = 1
map_dict[end]

for _ in range(N):
    start_point, end_point, cost = map(int, sys.stdin.readline().strip().split())
    if end_point - start_point > cost and end_point <= end:
        try:
            if map_dict[start_point][end_point] > cost:
                map_dict[start_point][end_point] = cost
        except KeyError:
            map_dict[start_point][end_point] = cost

result: dict = dijkstra(map_dict, 0)

print(f'{result[end]}')