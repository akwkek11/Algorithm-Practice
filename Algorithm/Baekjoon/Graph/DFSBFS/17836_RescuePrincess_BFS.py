from collections import deque

import copy
import sys

N, M, T = map(int, sys.stdin.readline().strip().split())
maze: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
step: list = [[float('inf') for _ in range(M)] for _ in range(N)]
sword_visit: list = [[0 for _ in range(M)] for _ in range(N)]
q: deque = deque(())

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

def bfs(x: int, y: int, sword: bool) -> None:
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M and (step[next_x][next_y] == float('inf') or (sword and sword_visit[next_x][next_y] == 0)):
            if (not sword and maze[next_x][next_y] != 1) or sword:
                step[next_x][next_y] = min(step[next_x][next_y], step[x][y] + 1) if not sword else step[x][y] + 1
                if maze[next_x][next_y] == 2 or sword:
                    sword_visit[next_x][next_y] = 1
                q.append((next_x, next_y, True)) if maze[next_x][next_y] == 2 else q.append((next_x, next_y, sword))

q.append((0, 0, False))
step[0][0] = 0
final_x: int = N - 1
final_y: int = M - 1

while q:
    target_x, target_y, have_sword = q.popleft()
    if (target_x, target_y) == (final_x, final_y):
        break
    bfs(target_x, target_y, have_sword)

print('Fail') if step[final_x][final_y] > T else print(f'{step[final_x][final_y]}')