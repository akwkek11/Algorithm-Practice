from collections import defaultdict

import heapq
import sys

def dijkstra(graph: defaultdict, start: str, final: str) -> (defaultdict, list):
    distances = defaultdict(lambda: float('inf'))
    parents = defaultdict(lambda: float('inf')) 
    for node in graph:
        distances[node]
        parents[node]
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
                parents[new_destination] = current_destination
                heapq.heappush(queue, [distance, new_destination])
    
    trace: list = [] 
    current: str = final
    while current != start: 
        trace.append(current)
        current = parents[current]
    trace.append(start)
    trace.reverse()

    return distances, trace

n: int = int(sys.stdin.readline().strip())
m: int = int(sys.stdin.readline().strip())
map_dict: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))

for i in range(1, n+1):
    map_dict[i]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    if map_dict[start][end] > cost:
        map_dict[start][end] = cost

start, end = map(int, sys.stdin.readline().strip().split())
res_dict, res_list = dijkstra(map_dict, start, end)
print(f'{res_dict[end]}')
print(f'{len(res_list)}')
for i in range(len(res_list)):
    print(f'{res_list[i]}', end = ' ') if i != len(res_list) - 1 else print(f'{res_list[i]}')