from collections import deque

import sys

def bfs(x: int, y: int, z: int) -> None:
    for i in range(len(dx)):
        next_x = x + dx[i]
        if 0 <= next_x < H and tomato_map[next_x][y][z] != -1 and is_visited[next_x][y][z] == 0:
            is_visited[next_x][y][z] = is_visited[x][y][z] + 1
            bfs_queue.append((next_x, y, z))
    for i in range(len(dy)):
        next_y = y + dy[i]
        next_z = z + dz[i]
        if 0 <= next_y < N and 0 <= next_z < M and tomato_map[x][next_y][next_z] != -1 and is_visited[x][next_y][next_z] == 0:
            is_visited[x][next_y][next_z] = is_visited[x][y][z] + 1
            bfs_queue.append((x, next_y, next_z))

M, N, H = map(int, sys.stdin.readline().strip().split())
tomato_map: list = [[[] for _ in range(N)] for _ in range(H)]
is_visited: list = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx: list = [1, -1]
dy: list = [-1, 1, 0, 0]
dz: list = [0, 0, -1, 1]

for i in range(H):
    for j in range(N):
        tomato_map[i][j] = list(map(int, sys.stdin.readline().strip().split()))

is_zero: bool = False
for i in range(H):
    for j in range(N):
        for k in tomato_map[i][j]:
            if k == 0:
                is_zero = True
                break

bfs_queue: deque = deque(())
if is_zero:
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato_map[i][j][k] == 1:
                    bfs_queue.append((i, j, k))
                    is_visited[i][j][k] = 1
                elif tomato_map[i][j][k] == -1:
                    is_visited[i][j][k] = -1

    max_try: int = 0
    while bfs_queue:
        target_x, target_y, target_z = bfs_queue.popleft()
        max_try = max(max_try, is_visited[target_x][target_y][target_z])
        bfs(target_x, target_y, target_z)

    is_not_tomato: bool = False
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if is_visited[i][j][k] == 0:
                    is_not_tomato = True
                    break
    
    print('-1') if is_not_tomato else print(f'{max_try - 1}')
else:
    print('0')