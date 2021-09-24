from collections import defaultdict

import heapq
import sys

# Dijsktra
def dijkstra(graph: defaultdict, start: str, end: str, node_num: int) -> defaultdict:
    distances: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for node in graph:
        distances[node]
    distances[start][node_num] = 0
    queue = []
    heapq.heappush(queue, [distances[start][node_num], start, node_num])

    while queue:
        current_distance, current_destination, num_of_node = heapq.heappop(queue)

        if distances[current_destination][num_of_node] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance: int = current_distance + new_distance
            min_distance: int = float('inf')
            target_index: int = float('inf')
            for key, value in distances[new_destination].items():
                if min_distance >= value:
                    min_distance = value
                    target_index = key

            if distance < distances[new_destination][num_of_node + 1] and not (distance >= min_distance and num_of_node + 1 >= target_index):
                distances[new_destination][num_of_node + 1] = distance
                if new_destination != end:
                    heapq.heappush(queue, [distance, new_destination, num_of_node + 1])

    return distances

N, M, K = map(int, sys.stdin.readline().strip().split())
map_dict: defaultdict = defaultdict(lambda : defaultdict(lambda : float('inf')))
for i in (1, N + 1):
    map_dict[i]

node_start, node_end = map(int, sys.stdin.readline().strip().split())

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    if map_dict[start][end] > cost:
        map_dict[end][start] = map_dict[start][end] = cost

result: defaultdict = dijkstra(map_dict, node_start, node_end, 0)
min_cost: int = float('inf')
for key, value in result[node_end].items():
    min_cost = min(min_cost, value)
print(f'{min_cost}')

for _ in range(K):
    p: int = int(sys.stdin.readline().strip())
    for key, value in result[node_end].items():
        result[node_end][key] += p * key

    min_cost = float('inf')
    min_index: int = 0
    for key, value in result[node_end].items():
        if min_cost >= value:
            min_cost = value
            min_index = key

    for key, value in list(result[node_end].items()):
        if key > min_index:
            result[node_end].pop(key)
    
    print(f'{min_cost}')