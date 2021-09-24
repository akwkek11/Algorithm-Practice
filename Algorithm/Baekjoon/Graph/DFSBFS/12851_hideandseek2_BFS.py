import sys
from collections import deque

step_map: list = [100002 for _ in range(100001)]
bfs_queue: deque = deque()
count: int = 0

def BFS(x: int) -> None:
    global step_map
    global bfs_queue
    
    if 0 <= x-1 < len(step_map) and step_map[x-1] > step_map[x]:
        step_map[x-1] = step_map[x] + 1
        bfs_queue.append(x-1)
    
    if 0 <= x+1 < len(step_map) and step_map[x+1] > step_map[x]:
        step_map[x+1] = step_map[x] + 1
        bfs_queue.append(x+1)
    
    if 0 <= 2*x < len(step_map) and step_map[2*x] > step_map[x]:
        step_map[2*x] = step_map[x] + 1
        bfs_queue.append(2*x)

start, end = map(int, sys.stdin.readline().strip().split())

step_map[start] = 0
bfs_queue.append(start)
while bfs_queue:
    target: int = bfs_queue.popleft()
    if target == end:
        count = 1
        while bfs_queue:
            surpass: int = bfs_queue.popleft()
            if surpass == end:
                count += 1
        break
    else:
        BFS(target)

print(f'{step_map[end]}')
print(f'{count}')