from collections import defaultdict

import heapq
import sys

# dijkstra
def dijkstra(graph: defaultdict, start: str, final: str, hi_sum: int) -> defaultdict:
    distances = defaultdict(lambda: defaultdict(lambda: float('inf')))
    distances[start][hi_sum] = 0
    queue = []
    heapq.heappush(queue, [distances[start][hi_sum], start, hi_sum])

    while queue:
        current_distance, current_destination, current_length = heapq.heappop(queue)
        
        if current_destination == final:
            break

        if distances[current_destination][current_length] < current_distance:
            continue

        for new_destination, new_data in graph[current_destination].items():
            for new_distance, new_length in new_data:
                distance = current_distance + new_distance
                length = current_length - new_length

                if length > 0 and distance < distances[new_destination][length]:
                    distances[new_destination][length] = distance
                    heapq.heappush(queue, [distance, new_destination, length])

    return distances

K, N, M = map(int, sys.stdin.readline().strip().split())
map_dict: defaultdict = defaultdict(lambda : defaultdict(list))

for i in range(1, N + 1):
    map_dict[i]

for _ in range(M):
    start, end, time, sub_length = map(int, sys.stdin.readline().strip().split())
    map_dict[start][end].append((time, sub_length))
    map_dict[end][start].append((time, sub_length))

start, end = map(int, sys.stdin.readline().strip().split())
res_data: defaultdict = dijkstra(map_dict, start, end, K)
min_cost: int = float('inf')
for key, value in res_data[end].items():
    min_cost = min(min_cost, value)
print(f'{min_cost}') if min_cost != float('inf') else print('-1')