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

N, M, X = map(int, sys.stdin.readline().strip().split())
map_dict: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    map_dict[start][end] = cost

results: list = [[]]
for i in range(1, N + 1):
    results.append(dijkstra(map_dict, i))

print(max([results[i][X] + results[X][i] for i in range(1, N + 1)]))