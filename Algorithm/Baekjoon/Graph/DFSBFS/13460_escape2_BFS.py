from collections import deque

import sys

N, M = map(int, sys.stdin.readline().strip().split())
escape_map: list = [[0 for _ in range(M)] for _ in range(N)]
str_map: list = [str(sys.stdin.readline().strip()) for _ in range(N)]
is_visited: list = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
str_list: list = ['.', '#', 'R', 'B', 'O']

# 맵 변환, 처음 위치 저장
q: deque = deque(())
rx, ry, bx, by = (0, 0, 0, 0)
for i in range(N):
    for j in range(M):
        if str_map[i][j] == 'R':
            rx = i
            ry = j
        elif str_map[i][j] == 'B':
            bx = i
            by = j

        escape_map[i][j] = str_list.index(str_map[i][j])
    
q.append((rx, ry, bx, by, 1))
is_visited[rx][ry][bx][by] = 1

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]
def move(x: int, y: int, move_x: int, move_y: int) -> tuple:
    count: int = 0
    while escape_map[x + move_x][y + move_y] != 1 and escape_map[x][y] != 4:
        x += move_x
        y += move_y
        count += 1
    
    return (x, y, count)

def bfs(rx: int, ry: int, bx: int, by: int, depth: int) -> None:
    global result
    for i in range(len(dx)):
        next_rx, next_ry, red_count = move(rx, ry, dx[i], dy[i])
        next_bx, next_by, blue_count = move(bx, by, dx[i], dy[i])

        if escape_map[next_bx][next_by] == 4:
            continue

        if escape_map[next_rx][next_ry] == 4:
            result = depth
            return

        if (next_rx, next_ry) == (next_bx, next_by):
            if red_count > blue_count:
                next_rx -= dx[i]
                next_ry -= dy[i]
            elif red_count < blue_count:
                next_bx -= dx[i]
                next_by -= dy[i]
        
        if is_visited[next_rx][next_ry][next_bx][next_by] == 0:
            is_visited[next_rx][next_ry][next_bx][next_by] = 1
            q.append((next_rx, next_ry, next_bx, next_by, depth + 1))

max_count: int = 10
result: int = -1
while q:
    red_x, red_y, blue_x, blue_y, now_depth = q.popleft()
    if now_depth > 10:
        break

    bfs(red_x, red_y, blue_x, blue_y, now_depth)
    if result != -1:
        break
print(f'{result}')