from collections import deque

import sys

'''
0 2 4 4 -> 2 0 4 4 -> 3 0 1 4 -> (1, 2), (0, 3) -> 1,0 ~ 2,3
'''
def bfs(x: int, y: int) -> None:
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < M and 0 <= next_y < N and paper_map[next_x][next_y] == 0 and is_visited[next_x][next_y] == 0:
            is_visited[next_x][next_y] = 1
            q.append((next_x, next_y))

M, N, K = map(int, sys.stdin.readline().strip().split())
paper_map: list = [[0 for _ in range(N)] for _ in range(M)]
is_visited: list = [[0 for _ in range(N)] for _ in range(M)]
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    convert_y1: int = M - y1
    convert_y2: int = M - y2
    for i in range(min(convert_y1, convert_y2), max(convert_y1, convert_y2)):
        for j in range(min(x1, x2), max(x1, x2)):
            paper_map[i][j] = 1

q: deque = deque(())
domain_size: list = []
domain_count: int = 0
for i in range(M):
    for j in range(N):
        if paper_map[i][j] == 0 and is_visited[i][j] == 0:
            domain_count = 0
            is_visited[i][j] = 1
            q.append((i, j))
            while q:
                target_x, target_y = q.popleft()
                domain_count += 1
                bfs(target_x, target_y)
            domain_size.append(domain_count)

domain_size.sort()
print(f'{len(domain_size)}')
for i in range(len(domain_size)):
    print(f'{domain_size[i]}', end=' ') if i != len(domain_size) - 1 else print(f'{domain_size[i]}')