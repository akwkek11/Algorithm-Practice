from collections import deque

import sys

N, M = map(int, sys.stdin.readline().strip().split())
cost: list = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
maze: list = [list(map(int, list(str(sys.stdin.readline().strip())))) for _ in range(N)]

Ex: int = N - 1
Ey: int = M - 1
result: int = -1

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]
def bfs(x: int, y: int, is_block: int) -> None:
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if maze[next_x][next_y] == 1 and is_block and cost[next_x][next_y][is_block] == 0:
                cost[next_x][next_y][is_block - 1] = cost[x][y][is_block] + 1
                bfs_queue.append((next_x, next_y, is_block - 1))
            elif maze[next_x][next_y] == 0 and cost[next_x][next_y][is_block] == 0:
                cost[next_x][next_y][is_block] = cost[x][y][is_block] + 1
                bfs_queue.append((next_x, next_y, is_block))

bfs_queue: deque = deque(())
cost[0][0][1] = 1
bfs_queue.append((0, 0, 1))
while bfs_queue:
    target_x, target_y, block = bfs_queue.popleft()
    if target_x == Ex and target_y == Ey:
        result = cost[target_x][target_y][block]
        bfs_queue.clear()
        break
    bfs(target_x, target_y, block)

print(f'{result}')