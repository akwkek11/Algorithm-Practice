from collections import deque
import sys

# 물 시뮬먼저, 그리고 비버 시뮬을 나중에
R, C = map(int, sys.stdin.readline().strip().split())
beaver_map: list = [[0 for _ in range(C)] for _ in range(R)]
is_visited: list = [[0 for _ in range(C)] for _ in range(R)]
str_map: list = []
for _ in range(R):
    str_map.append(list(map(str, sys.stdin.readline().strip())))

bfs_beaverqueue: deque = deque()
bfs_waterqueue: deque = deque()
count: int = 0
# 길 = 0, 비버 = 1, 물 = 2, 돌 = 3, 도착지 = 4
for i in range(R):
    for j in range(C):
        if str_map[i][j] == 'S':
            beaver_map[i][j] = 1
            is_visited[i][j] = 1
            bfs_beaverqueue.append((i, j, 0, 0))
        elif str_map[i][j] == '*':
            beaver_map[i][j] = 2
            is_visited[i][j] = 1
            bfs_beaverqueue.append((i, j, 1, 0))
        elif str_map[i][j] == 'X':
            beaver_map[i][j] = 3
        elif str_map[i][j] == 'D':
            beaver_map[i][j] = 4

# 타입 0 : 비버, 1 : 물
def bfs(x: int, y: int, object_type: int, count: int) -> None:
    dx: list = [-1, 1, 0, 0]
    dy: list = [0, 0, -1, 1]
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < R and 0 <= next_y < C:
            if object_type == 0:
                if is_visited[next_x][next_y] == 0 and beaver_map[next_x][next_y] not in [2, 3]:
                    is_visited[next_x][next_y] = 1
                    bfs_beaverqueue.append((next_x, next_y, object_type, count + 1))
            else:
                if is_visited[next_x][next_y] == 0 and beaver_map[next_x][next_y] not in [3, 4]:
                    is_visited[next_x][next_y] = 1
                    bfs_waterqueue.append((next_x, next_y, object_type, count + 1))

reach: bool = False
result: int = 0
# 번갈아 가면서 큐가 돌아가야 함.
while bfs_beaverqueue or bfs_waterqueue:
    while bfs_waterqueue:
        target_x, target_y, object_type, now_count = bfs_waterqueue.popleft()
        if now_count > count:
            bfs_waterqueue.appendleft((target_x, target_y, object_type, now_count))
            break
        bfs(target_x, target_y, object_type, now_count)
    while bfs_beaverqueue:
        target_x, target_y, object_type, now_count = bfs_beaverqueue.popleft()
        if beaver_map[target_x][target_y] == 4:
            reach = True
            result = now_count
            break
        if now_count > count:
            bfs_beaverqueue.appendleft((target_x, target_y, object_type, now_count))
            break
        bfs(target_x, target_y, object_type, now_count)
    if reach:
        break
    count += 1

if reach:
    print(result)
else:
    print('KAKTUS')