from collections import deque

import sys

N, M = map(int, sys.stdin.readline().strip().split())
ice_map: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

q: deque = deque(())
q2: deque = deque(())

def bfs(x: int, y: int) -> None:
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if is_visited[next_x][next_y] == 0:
            if ice_map[next_x][next_y] >= 1:
                is_visited[next_x][next_y] = 1
                q.append((next_x, next_y))
            else:
                ice_map[x][y] -= 1

    if ice_map[x][y] < 0:
        ice_map[x][y] = 0

ice_break_count: int = 0
is_none: bool = False
while True:

    # 빙산 덩어리 개수 체크하면서 녹이기
    ice_count: int = 0
    is_visited: list = [[0] * M for _ in range(N)]

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if ice_map[i][j] >= 1 and is_visited[i][j] == 0:
                is_visited[i][j] = 1
                q.append((i, j))
                ice_count += 1
                if ice_count > 1:
                    break
                while q:
                    target_x, target_y = q.popleft()
                    bfs(target_x, target_y)
    
    # 빙산이 2개 이상이거나? 0개면 break
    if ice_count != 1:

        # 만약 빙산이 0개면 나눠진 적이 없으므로 count는 0
        if ice_count == 0:
            is_none = True
        break

    ice_break_count += 1

if is_none:
    ice_break_count = 0
print(f'{ice_break_count}')