from collections import deque

import sys

N, M, K = map(int, sys.stdin.readline().strip().split())

maze: list = [list(map(int, str(sys.stdin.readline().strip()))) for _ in range(N)]
cost: list = [[[0 for _ in range(11)] for _ in range(M)] for _ in range(N)]
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

bfs_queue: deque = deque(())

def bfs(x: int, y: int, is_block: int) -> None:
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if maze[next_x][next_y] == 1 and is_block and cost[next_x][next_y][is_block - 1] == 0:
                cost[next_x][next_y][is_block - 1] = cost[x][y][is_block] + 1
                bfs_queue.append((next_x, next_y, is_block - 1))
            elif maze[next_x][next_y] == 0 and cost[next_x][next_y][is_block] == 0:
                cost[next_x][next_y][is_block] = cost[x][y][is_block] + 1
                bfs_queue.append((next_x, next_y, is_block))

result: int = -1
bfs_queue.append((0, 0, K))
cost[0][0][K] = 1
while bfs_queue:
    target_x, target_y, block = bfs_queue.popleft()
    if target_x == N - 1 and target_y == M - 1:
        result = cost[target_x][target_y][block]
        bfs_queue.clear()
        break
    bfs(target_x, target_y, block)

print(f'{result}')