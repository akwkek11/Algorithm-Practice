from collections import defaultdict

import sys

# Bellman Ford
def bellman_ford(graph: defaultdict, start: int) -> object:
    distance, predecessor = defaultdict(lambda : float('inf')), defaultdict(lambda : None)
    for node in graph:  
        distance[node]
        predecessor[node]
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    distance[neighbor] = distance[node] + graph[node][neighbor]
                    predecessor[neighbor] = node

    for node in graph:
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                return -1, "Cycle Detected"

    return distance, predecessor

N, M = map(int, sys.stdin.readline().strip().split())
road_dict: defaultdict = defaultdict(lambda : defaultdict(lambda : float('inf')))
for i in range(1, N + 1):
    road_dict[i]
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    road_dict[start][end] = min(road_dict[start][end], cost)

res_dict, predecessor = bellman_ford(road_dict, 1)
if res_dict == -1:
    print('-1')
else:
    for i in range(2, N + 1):
        print(f'{res_dict[i]}') if res_dict[i] != float('inf') else print('-1')