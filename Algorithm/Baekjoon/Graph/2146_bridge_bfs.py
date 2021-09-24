from collections import deque

import sys

N: int = int(sys.stdin.readline().strip())
island_map: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
is_visited: list = [[0 for _ in range(N)] for _ in range(N)]
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

bfs_queue: deque = deque(())
reset: deque = deque(())
def mask_bfs(x: int, y: int) -> None:
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if island_map[next_x][next_y] > 0 and is_visited[next_x][next_y] == 0:
                is_visited[next_x][next_y] = 1
                island_map[next_x][next_y] = island_number
                bfs_queue.append((next_x, next_y))
                reset.append((next_x, next_y))

def length_bfs(start: int, x: int, y: int, count: int, is_met: bool) -> None:
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if island_map[next_x][next_y] == 0 and is_visited[next_x][next_y] == 0:
                is_visited[next_x][next_y] = 1
                bfs_queue.append((start, next_x, next_y, count + 1, False))
                reset.append((next_x, next_y))
            elif island_map[next_x][next_y] > 0 and island_map[next_x][next_y] != start:
                bfs_queue.append((start, next_x, next_y, count + 1, True))
                
# step 1 : 섬에 숫자 부여
island_number: int = 0
for i in range(N):
    for j in range(N):
        if island_map[i][j] > 0 and is_visited[i][j] == 0:
            island_number += 1
            island_map[i][j] = island_number
            is_visited[i][j] = 1
            bfs_queue.append((i, j))
            reset.append((i, j))
            
            while bfs_queue:
                target_x, target_y = bfs_queue.popleft()
                mask_bfs(target_x, target_y)

while reset:
    target_x, target_y = reset.popleft()
    is_visited[target_x][target_y] = 0

# step 2 : 각 섬마다 거리계산 시작
min_length: int = float('inf')
for i in range(N):
    for j in range(N):
        if island_map[i][j] > 0 and is_visited[i][j] == 0:
            is_visited[i][j] = 1
            bfs_queue.append((island_map[i][j], i, j, 0, False))
            reset.append((i, j))

            while bfs_queue:
                start, target_x, target_y, now_count, now_met = bfs_queue.popleft()

                if now_met:
                    if start != island_map[target_x][target_y]:
                        min_length = min(min_length, now_count - 1)
                        bfs_queue.clear()
                        while reset:
                            target_x, target_y = reset.popleft()
                            is_visited[target_x][target_y] = 0
                    continue
                
                if min_length == 1:
                    break
                length_bfs(start, target_x, target_y, now_count, now_met)

print(f'{min_length}')