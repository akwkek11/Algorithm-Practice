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
            distance: int = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    
    return distances

test_case: int = int(sys.stdin.readline().strip())

for _ in range(test_case):
    map_dict: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))
    n, d, c = map(int, sys.stdin.readline().strip().split())
    for _ in range(d):
        end, start, cost = map(int, sys.stdin.readline().strip().split())
        map_dict[start][end] = cost
    
    results: defaultdict = dijkstra(map_dict, c)
    print(len(results.keys()), max(results.values()))