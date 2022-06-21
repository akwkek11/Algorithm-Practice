from collections import deque
import sys
from typing import List

# input
F, S, G, U, D = map(int, sys.stdin.readline().strip().split())

# 전체 최소 이동 횟수
total: List[int] = [0 for _ in range(F + 1)]

# 첫 시작은 1번째로 간주, 최소 이동횟수의 결과는 여기서 -1해주면 됨.
total[S] = 1

# bfs
bfs_queue: deque = deque(())

def BFS(now: int, step: int, up: int, down: int, maximum: int, minimum: int) -> None:
    global total
    
    if now + up <= maximum and total[now + up] == 0:
        total[now + up] = step + 1
        bfs_queue.append((now + up, step + 1))
    
    if now - down > 0 and total[now - down] == 0:
        total[now - down] = step + 1
        bfs_queue.append((now - down, step + 1))

    return

bfs_queue.append((S, total[S]))
result: int = float('inf')
while bfs_queue:
    now, step = bfs_queue.popleft()
    
    if now == G:
        result = step - 1
        break
    
    BFS(now, step, U, D, F, 0)

if result == float('inf'):
    print("use the stairs")
else:
    print(result)