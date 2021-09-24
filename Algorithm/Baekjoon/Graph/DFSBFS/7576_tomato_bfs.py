import sys
from collections import deque
from typing import List

M, N = map(int, sys.stdin.readline().strip().split())
tomato_map: List[int] = []
is_visited: List[int] = [[0 for _ in range(M)] for _ in range(N)]
is_zero: bool = False

dx: List[int] = [-1, 1, 0, 0]
dy: List[int] = [0, 0, -1, 1]

bfs_queue: deque = deque(())

block: int = 0
count: int = 0
day: int = 0

def BFS(x: int, y: int, step: int) -> None:
    global count
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < N and 0 <= next_y < M and is_visited[next_x][next_y] == 0 and tomato_map[next_x][next_y] != -1:
            tomato_map[next_x][next_y] = step + 1
            is_visited[next_x][next_y] = 1
            bfs_queue.append((next_x, next_y, tomato_map[next_x][next_y]))
            count += 1

for _ in range(N):
    tomato_map.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    for j in range(M):
        if tomato_map[i][j] == 1:
            tomato_map[i][j] = 0
            bfs_queue.append((i, j, tomato_map[i][j]))
            is_visited[i][j] = 1
            count += 1

        elif tomato_map[i][j] == 0 and is_zero == False:
            is_zero = True
        
        elif tomato_map[i][j] == -1:
            block += 1

if is_zero:
    while bfs_queue:
        target_x, target_y, now_step = bfs_queue.popleft()
        if day < now_step:
            day = now_step
        BFS(target_x, target_y, now_step)

    if count + block != M*N:
        day = -1

print(f'{day}')