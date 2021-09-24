from collections import deque

import sys

def bfs(x: int, y: int) -> None:
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < M and 0 <= next_y < N and banner[next_x][next_y] == 1 and is_visited[next_x][next_y] == 0:
            is_visited[next_x][next_y] = 1
            q.append((next_x, next_y))

M, N = map(int, sys.stdin.readline().strip().split())
banner: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
is_visited: list = [[0 for _ in range(N)] for _ in range(M)]
q: deque = deque(())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

count: int = 0
for i in range(M):
    for j in range(N):
        if banner[i][j] == 1 and is_visited[i][j] == 0:
            count += 1
            is_visited[i][j] = 1
            q.append((i, j))
            while q:
                target_x, target_y = q.popleft()
                bfs(target_x, target_y)

print(f'{count}')