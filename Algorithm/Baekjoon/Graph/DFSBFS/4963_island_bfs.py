from collections import deque

import sys

def bfs(x: int, y: int) -> None:
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < N and 0 <= next_y < M and banner[next_x][next_y] == 1 and is_visited[next_x][next_y] == 0:
            is_visited[next_x][next_y] = 1
            q.append((next_x, next_y))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    M, N = map(int, sys.stdin.readline().strip().split())
    banner: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    is_visited: list = [[0 for _ in range(M)] for _ in range(N)]
    q: deque = deque(())
    count: int = 0

    if M == 0 and N == 0:
        break

    for i in range(N):
        for j in range(M):
            if banner[i][j] == 1 and is_visited[i][j] == 0:
                count += 1
                is_visited[i][j] = 1
                q.append((i, j))
                while q:
                    target_x, target_y = q.popleft()
                    bfs(target_x, target_y)

    print(f'{count}')