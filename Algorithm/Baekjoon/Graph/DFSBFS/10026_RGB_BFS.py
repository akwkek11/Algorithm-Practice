from collections import deque

import sys

N: int = int(sys.stdin.readline().strip())
color_map: list = [str(sys.stdin.readline().strip()) for _ in range(N)]
is_visited: list = [[0 for _ in range(N)] for _ in range(N)]
q: deque = deque(())

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

def bfs(x: int, y: int, case: int) -> None:
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if case == 0:
            if 0 <= next_x < N and 0 <= next_y < N and is_visited[next_x][next_y] == 0 and color_map[next_x][next_y] == color_map[x][y]:
                is_visited[next_x][next_y] = 1
                q.append((next_x, next_y))
        else:
            if 0 <= next_x < N and 0 <= next_y < N and is_visited[next_x][next_y] == 0:
                if (color_map[x][y] in ['R', 'G'] and color_map[next_x][next_y] in ['R', 'G']) or (color_map[next_x][next_y] == color_map[x][y]):
                    is_visited[next_x][next_y] = 1
                    q.append((next_x, next_y))
original_count: int = 0
for i in range(N):
    for j in range(N):
        if is_visited[i][j] == 0:
            is_visited[i][j] = 1
            original_count += 1
            q.append((i, j))
            while q:
                target_x, target_y = q.popleft()
                bfs(target_x, target_y, 0)

for i in range(N):
    for j in range(N):
        is_visited[i][j] = 0

color_count: int = 0
for i in range(N):
    for j in range(N):
        if is_visited[i][j] == 0:
            is_visited[i][j] = 1
            color_count += 1
            q.append((i, j))
            while q:
                target_x, target_y = q.popleft()
                bfs(target_x, target_y, 1)

print(f'{original_count} {color_count}')