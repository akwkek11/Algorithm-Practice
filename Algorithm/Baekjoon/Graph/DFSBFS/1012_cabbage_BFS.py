import sys
from collections import deque

step = int(sys.stdin.readline().strip())
cabbage_map: list = []
is_visited: list = []
bfs_queue: deque = deque(())
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

def BFS(x: int, y: int) -> None:
    global cabbage_map
    global is_visited
    global bfs_queue
    global dx
    global dy

    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < N and 0 <= next_y < M and is_visited[next_x][next_y] == 0 and cabbage_map[next_x][next_y] == 1:
            is_visited[next_x][next_y] = 1
            bfs_queue.append((next_x, next_y))

for _ in range(step):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    cabbage_map = [[0 for _ in range(M)] for _ in range(N)]
    is_visited = [[0 for _ in range(M)] for _ in range(N)]
    count: int = 0

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().strip().split())
        cabbage_map[b][a] = 1

    for i in range(N):
        for j in range(M):
            if is_visited[i][j] == 0 and cabbage_map[i][j] == 1:
                count += 1
                bfs_queue.append((i, j))

            while bfs_queue:
                target_i, target_j = bfs_queue.popleft()
                is_visited[target_i][target_j] = 1
                BFS(target_i, target_j)

    print(f'{count}')