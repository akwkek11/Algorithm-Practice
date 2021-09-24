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

N, K = map(int, sys.stdin.readline().strip().split())
times: list = [[3,1,5], [3,2,2], [2,1,2], [3,4,1], [4,5,1], [5,6,1], [6,7,1], [7,8,1], [8,1,1]]
time_dict: defaultdict = defaultdict(dict)
for i in range(N):
    time_dict[i+1]
for i in times:
    time_dict[i[0]][i[1]] = i[2]

res_dict: dict = dijkstra(time_dict, K)
max_step: int = max(res_dict.values())
print('-1') if max_step == float('inf') else print(f'{max_step}')