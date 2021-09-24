from collections import defaultdict

import heapq
import sys

# Dijsktra
def dijkstra(graph: defaultdict, start: str) -> defaultdict:
    distances: defaultdict = defaultdict(lambda: float('inf'))
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

V, E = map(int, sys.stdin.readline().strip().split())

# 길 저장, 양방향
road_map: defaultdict = defaultdict(lambda : defaultdict(lambda : float('inf')))

# 맥도날드, 스타벅스 저장
build_map1: defaultdict = defaultdict(int)
build_map2: defaultdict = defaultdict(int)

for i in range(1, V + 1):
    road_map[i]

for i in range(V + 1, V + 3):
    road_map[i]

for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    road_map[start][end] = road_map[end][start] = cost

mcdonald_number, mcdonald_length = map(int, sys.stdin.readline().strip().split())
mcdonald_list: list = list(map(int, sys.stdin.readline().strip().split()))
while mcdonald_list:
    build_map1[mcdonald_list.pop()] = 1

starbucks_number, starbucks_length = map(int, sys.stdin.readline().strip().split())
starbucks_list: list = list(map(int, sys.stdin.readline().strip().split()))
while starbucks_list:
    build_map2[starbucks_list.pop()] = 1

for key in build_map1.keys():
    road_map[V + 1][key] = 0

for key in build_map2.keys():
    road_map[V + 2][key] = 0

mc_result: defaultdict = dijkstra(road_map, V + 1)
st_result: defaultdict = dijkstra(road_map, V + 2)

min_length: int = float('inf')
for i in range(1, V + 1):
    if 0 < mc_result[i] <= mcdonald_length and 0 < st_result[i] <= starbucks_length:
        min_length = min(min_length, mc_result[i] + st_result[i])

print(f'{min_length}') if min_length != float('inf') else print('-1')