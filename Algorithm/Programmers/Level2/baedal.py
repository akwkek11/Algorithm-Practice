from typing import List
from collections import defaultdict, deque

def solution(N: int, road: List[List[int]], K: int) -> int:
    shortest: List[int] = [float('inf') for _ in range(N + 1)]
    shortest[1] = 0
    road_map: defaultdict = defaultdict(lambda: float('inf'))
    road_connect: defaultdict = defaultdict(list)
    for start, end, cost in road:
        road_map[(start, end)] = min(road_map[(start, end)], cost)
        road_map[(end, start)] = min(road_map[(end, start)], cost)
        road_connect[start].append(end)
        road_connect[end].append(start)

    bfs_queue: deque = deque()
    bfs_queue.append((1, 1, 0))
    while bfs_queue:
        start, end, total = bfs_queue.popleft()
        for dest in road_connect[end]:
            init_list: List[tuple] = []
            if total + road_map[(end, dest)] <= K:
                init_list.append((end, dest, total + road_map[(end, dest)]))
            init_list.sort(key=lambda x : x[2])
            for road in init_list:
                if shortest[road[1]] > road[2]:
                    shortest[road[1]] = road[2]
                    bfs_queue.append(road)
    
    return len(shortest) - shortest.count(float('inf'))

print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))