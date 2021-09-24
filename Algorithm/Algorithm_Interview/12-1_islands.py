from collections import deque

import sys

def bfs(x: int, y: int) -> None:
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M and is_visited[next_x][next_y] == 0 and island_map[next_x][next_y] == 1:
            is_visited[next_x][next_y] = 1
            bfs_queue.append((next_x, next_y))

M, N = map(int, sys.stdin.readline().strip().split())
island_map: list = []
is_visited: list = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    island_map.append(list(map(int, list(str(sys.stdin.readline().strip())))))

island_count: int = 0
bfs_queue: deque = deque(())
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]
for i in range(N):
    for j in range(M):
        if island_map[i][j] == 1 and is_visited[i][j] == 0:
            island_count += 1
            is_visited[i][j] = 1
            bfs_queue.append((i, j))
            while bfs_queue:
                target_x, target_y = bfs_queue.popleft()
                bfs(target_x, target_y)

print(f'{island_count}')
        