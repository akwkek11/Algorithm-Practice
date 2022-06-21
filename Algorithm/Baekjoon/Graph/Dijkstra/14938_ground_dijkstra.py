from collections import defaultdict
import heapq
import sys

def dijkstra(graphs: defaultdict, start: int) -> defaultdict:
    distances: defaultdict = defaultdict(lambda: float('inf'))
    distances[start] = 0
    queue: heapq = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graphs[current_destination].items():
            distance = current_distance + new_distance

            if distances[new_destination] > distance:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances

n, m, r = map(int, sys.stdin.readline().strip().split())
item_count: list = list(map(int, sys.stdin.readline().strip().split()))
map_dict: defaultdict = defaultdict(lambda : defaultdict(lambda : float('inf')))
max_item: int = -float('inf')

for _ in range(r):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    map_dict[start][end] = cost
    map_dict[end][start] = cost

for i in range(1, n + 1):
    results: defaultdict = dijkstra(map_dict, i)
    max_item = max(max_item, sum([item_count[j - 1] for j in results.keys() if results[j] <= m]))

print(max_item)