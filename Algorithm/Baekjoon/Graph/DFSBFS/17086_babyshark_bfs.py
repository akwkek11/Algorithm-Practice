import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

shark_map: list = [[] for _ in range(N)]
is_visited: list = [[0 for _ in range(M)] for _ in range(N)]
is_visited_queue: deque = deque(())
met: bool = False
dx: list = [-1, 1, 0, 0, -1, -1, 1, 1]
dy: list = [0, 0, -1, 1, -1, 1, -1, 1]
depth: int = 0
try_count: list = [0 for i in range(101)]
bfs_queue: deque = deque(())
maximum_depth: int = 0
is_shark: bool = False

def BFS(x, y):
    global shark_map
    global is_visited
    global met
    global dx
    global dy
    global depth
    global try_count

    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < N and 0 <= next_y < M and is_visited[next_x][next_y] == 0:
            if shark_map[next_x][next_y] == 1:
                met = True
                break
            else:
                is_visited[next_x][next_y] = 1
                bfs_queue.append((next_x, next_y))
                is_visited_queue.append((next_x, next_y))
                try_count[depth] += 1
                
for i in range(N):
    shark_map[i].extend(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    for j in shark_map[i]:
        if j == 1:
            is_shark = True
            break

if is_shark:
    for i in range(N):
        for j in range(M):
            if shark_map[i][j] == 0:
                bfs_queue.append((i, j))
                is_visited_queue.append((i, j))

                depth = 0
                while bfs_queue:
                    if depth != 0:
                        if try_count[depth-1] <= 0:
                            depth += 1
                    else:
                        depth = 1

                    target_i, target_j = bfs_queue.popleft()
                    try_count[depth-1] -= 1

                    is_visited[target_i][target_j] = 1
                    BFS(target_i, target_j)

                    if met:
                        while bfs_queue:
                            bfs_queue.popleft()
                        maximum_depth = max(maximum_depth, depth)
                        break

                while is_visited_queue:
                    target_i, target_j = is_visited_queue.popleft()
                    is_visited[target_i][target_j] = 0

                for k in range(len(try_count)):
                    try_count[k] = 0

                met = False
                
print(maximum_depth)