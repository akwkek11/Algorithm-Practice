from collections import defaultdict

import heapq
import sys

def dijkstra(graph: defaultdict, start: str, end: str, count: int) -> dict:
    distances: dict = {node: float('inf') for node in graph}
    distances[start] = 0
    queue: list = []
    heapq.heappush(queue, [distances[start], start, 0])

    new_steps: bool = False
    while queue:
        current_distance, current_destination, current_count = heapq.heappop(queue)
        # print(current_distance, current_destination, current_count)
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance

            if new_destination != end:
                new_steps: bool = True
                current_count += 1

            if current_count <= count and distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination, current_count])
            
            if new_steps:
                new_steps = False
                current_count -= 1

    return distances

N = int(sys.stdin.readline().strip())
times: list = [[0,1,100], [1,2,100], [0,2,500]]
time_dict: defaultdict = defaultdict(dict)
for i in range(N):
    time_dict[i+1]
for i in times:
    time_dict[i[0]][i[1]] = i[2]

src, dst, K = map(int, sys.stdin.readline().strip().split())

res_dict: dict = dijkstra(time_dict, src, dst, K)
print('-1') if res_dict[dst] == float('inf') else print(f'{res_dict[dst]}')