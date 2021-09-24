import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().strip().split())

running_map: list = ['' for _ in range(N)]
answer: list = [[10000000 for _ in range(M)] for _ in range(N)]

for i in range(len(running_map)):
    running_map[i] = str(sys.stdin.readline().strip())

x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

answer[x1][y1] = 0

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

bfs_queue: deque = deque(())

def BFS(x, y):
    global running_map
    global answer
    global dx
    global dy
    
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        step = 1
        while step <= K and 0 <= next_x < N and 0 <= next_y < M and answer[next_x][next_y] >= answer[x][y] and running_map[next_x][next_y] != '#':
            if answer[next_x][next_y] == 10000000:
                bfs_queue.append((next_x, next_y))
                answer[next_x][next_y] = answer[x][y] + 1
            else:
                answer[next_x][next_y] = min(answer[next_x][next_y], answer[x][y] + 1)
                
            next_x += dx[i]
            next_y += dy[i]
            step += 1

bfs_queue.append((x1, y1))
while bfs_queue:
    target_x, target_y = bfs_queue.popleft()
    BFS(target_x, target_y)

if answer[x2][y2] == 10000000:
    print('-1')
else:
    print(f'{answer[x2][y2]}')