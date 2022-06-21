from collections import defaultdict
import heapq
import sys

def dijkstra(graph: defaultdict, start: tuple, start_cost: int) -> defaultdict:
    distances: defaultdict = defaultdict(lambda: float('inf'))

    # 시작은 (0, 0) 고정이니까.
    distances[start] = start_cost
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

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]
count: int = 1
while True:
    size = int(sys.stdin.readline().strip())
    
    if not size:
        break
    
    map_dict: defaultdict = defaultdict(lambda : defaultdict(lambda : float('inf')))
    distances_list: list = []
    for _ in range(size):
        distances_list.append(list(map(int, sys.stdin.readline().strip().split())))
    
    start_cost: int = distances_list[0][0]
    for i, j in [(a, b) for b in range(size) for a in range(size)]:
        for k in range(len(dx)):
            next_x: int = i + dx[k]
            next_y: int = j + dy[k]
            if 0 <= next_x < size and 0 <= next_y < size:
                map_dict[(i, j)][(next_x, next_y)] = distances_list[next_x][next_y]
                map_dict[(next_x, next_y)][(i, j)] = distances_list[i][j]
    
    results: defaultdict = dijkstra(map_dict, (0, 0), start_cost)
    print(f"Problem {count}: {results[(size - 1, size - 1)]}")
    count += 1