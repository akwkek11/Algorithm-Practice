import sys
from collections import deque

step: int = int(sys.stdin.readline().strip())
chess_map: list = []
bfs_queue: deque = deque(())
dx: list = [-1, -2, -2, -1, 1, 2, 2, 1]
dy: list = [-2, -1, 1, 2, -2, -1, 1, 2]

def BFS(x: int, y: int) -> None:
    global chess_map
    global bfs_queue
    global dx
    global dy

    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < l and 0 <= next_y < l and chess_map[next_x][next_y] == 100000:
            chess_map[next_x][next_y] = chess_map[x][y] + 1
            bfs_queue.append((next_x, next_y))

for _ in range(step):
    l: int = int(sys.stdin.readline().strip())
    chess_map = [[100000 for _ in range(l)] for _ in range(l)]

    start_x, start_y = map(int, sys.stdin.readline().strip().split())
    chess_map[start_x][start_y] = 0
    target_x, target_y = map(int, sys.stdin.readline().strip().split())

    bfs_queue.append((start_x, start_y))
    while bfs_queue:
        target_i, target_j = bfs_queue.popleft()
        if target_i == target_x and target_j == target_y:
            while bfs_queue:
                bfs_queue.popleft()
            break
        else:
            BFS(target_i, target_j)

    print(f'{chess_map[target_x][target_y]}')