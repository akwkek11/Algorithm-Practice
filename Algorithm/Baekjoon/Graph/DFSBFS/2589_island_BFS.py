'''
2021-07-31
'''
from collections import deque

import sys

def bfs(x: int, y: int, size_x: int, size_y: int) -> int:
    '''
        https://www.acmicpc.net/problem/2589
    '''
    is_visited: list = [[0 for _ in range(size_y)] for _ in range(size_x)]
    q: deque = deque(())
    q.append((x, y, 0))
    is_visited[x][y] = 1
    max_step: int = 0
    while q:
        target_x, target_y, now_step = q.popleft()
        max_step = max(max_step, now_step)
        for i in range(len(dx)):
            next_x: int = target_x + dx[i]
            next_y: int = target_y + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N and is_visited[next_x][next_y] == 0 and island_map[next_x][next_y] == 'L':
                q.append((next_x, next_y, now_step + 1))
                is_visited[next_x][next_y] = 1

    return max_step

M, N = map(int, sys.stdin.readline().strip().split())
island_map: list = [list(map(str, sys.stdin.readline().strip())) for _ in range(M)]
start_visited: list = [[0 for _ in range(N)] for _ in range(M)]
init_queue: deque = deque(())
start_queue: deque = deque(())
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

max_depth: int = -float('inf')
for i in range(M):
    for j in range(N):
        if island_map[i][j] == 'L' and start_visited[i][j] == 0:
            start_visited[i][j] = 1
            init_queue.append((i, j))
            while init_queue:
                target_i, target_j = init_queue.popleft()
                flag: bool = True
                for k in range(len(dx)):
                    next_i: int = target_i + dx[k]
                    next_j: int = target_j + dy[k]
                    if 0 <= next_i < M and 0 <= next_j < N:
                        if start_visited[next_i][next_j] == 0 and island_map[next_i][next_j] == 'L':
                            flag = False
                            init_queue.append((next_i, next_j))
                            start_visited[next_i][next_j] = 1
                if flag:
                    start_queue.append((target_i, target_j))             

while start_queue:
    i, j = start_queue.popleft()
    max_depth = max(max_depth, bfs(i, j, M, N))

print(f'{max_depth}')