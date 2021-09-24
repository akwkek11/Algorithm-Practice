import sys
from collections import deque

W, H = map(int, sys.stdin.readline().strip().split())
razor_map: list = [str(sys.stdin.readline().strip()) for _ in range(H)]
convert_razor_map: list = [[0 for _ in range(W)] for _ in range(H)]

q: deque = deque(())
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]
answer: list = [[float('inf') for _ in range(W)] for _ in range(H)]

find_start: bool = False
for i in range(H):
    for j in range(W):
        if razor_map[i][j] == '*':
            convert_razor_map[i][j] = 1
        elif razor_map[i][j] == 'C':
            if not find_start:
                find_start = True
                convert_razor_map[i][j] = 2
                q.append((i, j))
                answer[i][j] = 0
            else:
                convert_razor_map[i][j] = 3


def BFS(x, y):
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        while 0 <= next_x < H and 0 <= next_y < W and answer[next_x][next_y] >= answer[x][y] and convert_razor_map[next_x][next_y] != 1:
            if answer[next_x][next_y] == float('inf'):
                q.append((next_x, next_y))
                answer[next_x][next_y] = answer[x][y] + 1
            else:
                answer[next_x][next_y] = min(answer[next_x][next_y], answer[x][y] + 1)
                
            next_x += dx[i]
            next_y += dy[i]

final_x: int = 0
final_y: int = 0
while q:
    target_x, target_y = q.popleft()
    if convert_razor_map[target_x][target_y] == 3:
        final_x, final_y = target_x, target_y
        break
    else:
        BFS(target_x, target_y)

res: int = answer[final_x][final_y] - 1
print(f'{res}')
