import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
virus: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
queue: deque = deque()
virus_count: list = [0, 1, 1, 0]

def BFS(x: int, y: int, virus_type: int):
    dx: list = [1, -1, 0, 0]
    dy: list = [0, 0, -1, 1]

    for i in range(4):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]

        if 0 <= next_x < N and 0 <= next_y < M and virus[next_x][next_y] == 0:
            third_virus: bool = False
            if virus_type == 1:
                for i in range(4):
                    check_x: int = next_x + dx[i]
                    check_y: int = next_y + dy[i]
                    if 0 <= check_x < N and 0 <= check_y < M and virus_type + virus[check_x][check_y] == 3:
                        third_virus = True
                        break
            
            if third_virus:
                virus[next_x][next_y] = 3
                virus_count[3] += 1
            else:
                virus[next_x][next_y] = virus_type
                queue.append((next_x, next_y, virus_type))
                virus_count[virus_type] += 1

for i in range(N):
    for j in range(M):
        if virus[i][j] == 1:
            queue.append((i, j, 1))
        elif virus[i][j] == 2:
            queue.append((i, j, 2))

first_x, first_y, first_type = queue.popleft()
if first_type == 2:
    queue.append((first_x, first_y, first_type))
else: 
    queue.appendleft((first_x, first_y, first_type))

while queue:
    x, y, virus_type = queue.popleft()
    BFS(x, y, virus_type)

print(f"{virus_count[1]} {virus_count[2]} {virus_count[3]}")