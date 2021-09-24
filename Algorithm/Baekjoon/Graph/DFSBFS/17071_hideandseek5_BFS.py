import sys
from collections import deque

step_map: list = [[1000000, 1000000] for _ in range(500001)]
max_size: int = 500000
bfs_queue: deque = deque(())
is_found: bool = False
step_count: int = 0

def BFS(x: int, step: int) -> None:
    global step_map
    global bfs_queue
        
    if 0 <= x-1:
        if step_map[x-1][0] == 1000000:
            step_map[x-1][0] = step + 1
            bfs_queue.append((x-1, step+1))
        elif step_map[x-1][1] == 1000000:
            if step_map[x-1][0]%2 == step%2:
                step_map[x-1][1] = step + 1
                bfs_queue.append((x-1, step+1))
    
    if x+1 <= max_size:
        if step_map[x+1][0] == 1000000:
            step_map[x+1][0] = step + 1
            bfs_queue.append((x+1, step+1))
        elif step_map[x+1][1] == 1000000:
            if step_map[x+1][0]%2 == step%2:
                step_map[x+1][1] = step + 1
                bfs_queue.append((x+1, step+1))
    
    if 2*x <= max_size:
        if step_map[2*x][0] == 1000000:
            step_map[2*x][0] = step + 1
            bfs_queue.append((2*x, step+1))
        elif step_map[2*x][1] == 1000000:
            if step_map[2*x][0]%2 == step%2:
                step_map[2*x][1] = step + 1
                bfs_queue.append((2*x, step+1))

start, end = map(int, sys.stdin.readline().strip().split())

step_map[start][0] = 0
bfs_queue.append((start, 0))
while bfs_queue:
    target, now_step = bfs_queue.popleft()
    BFS(target, now_step)

while end <= 500000:
    if step_map[end][0] == step_count or step_map[end][1] == step_count:
        is_found = True
        break

    elif (step_map[end][0] < step_count and (step_map[end][0])%2 == step_count%2) or (step_map[end][1] < step_count and (step_map[end][1])%2 == step_count%2):
        is_found = True
        break
    step_count += 1
    end += step_count

if is_found:
    print(f'{step_count}')
else:
    print('-1')