import sys
from collections import deque 

N, M = map(int, sys.stdin.readline().strip().split())
war_map: list = ['' for _ in range(M)]
is_visited: list = [[0 for _ in range(N)] for _ in range(M)]

for i in range(M):
    war_map[i] = str(sys.stdin.readline().strip())

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]
war_strength: list = [0, 0]
bfs_queue: deque = deque(())
count: int = 0
add_target: int = 0

def BFS(x, y):
    global war_map
    global is_visited
    global dx
    global dy
    global bfs_queue

    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]

        if 0 <= next_x < M and 0 <= next_y < N and is_visited[next_x][next_y] == 0 and war_map[x][y] == war_map[next_x][next_y]:
            is_visited[next_x][next_y] = 1
            bfs_queue.append((next_x, next_y))

for i in range(M):
    for j in range(N):
        if is_visited[i][j] == 0:
            bfs_queue.append((i, j))
            while bfs_queue:
                target_i, target_j = bfs_queue.popleft()
                if war_map[target_i][target_j] == 'W':
                    add_target = 0
                else:
                    add_target = 1
                is_visited[target_i][target_j] = 1
                count += 1
                BFS(target_i, target_j)
                
            war_strength[add_target] += count ** 2
            
            count = 0

print(f'{war_strength[0]}',end=' ')
print(f'{war_strength[1]}',end='')