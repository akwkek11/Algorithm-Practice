from collections import deque

import heapq
import sys

M, N = map(int, sys.stdin.readline().strip().split())

maze: list = [list(map(int, str(sys.stdin.readline().strip()))) for _ in range(N)]
cost: list = [[-1 for _ in range(M)] for _ in range(N)]
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

# queue : 섬의 넓이 체크 용도로 사용
# heap : 벽 부수면서 다른 섬 찾아갈 때 사용
queue: deque = deque(())
heap: heapq = []

# 섬 넓이 체크
def bfs1(break_wall: int, x: int, y: int) -> None:
    is_outside: bool = False
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if maze[next_x][next_y] == 0 and cost[next_x][next_y] == -1:
                cost[next_x][next_y] = break_wall
                queue.append((break_wall, next_x, next_y))
            elif maze[next_x][next_y] == 1 and not is_outside:
                heapq.heappush(heap, (break_wall, x, y))
                is_outside = True

# 벽 부수면서 다른 섬 체크
def bfs2(break_wall: int, x: int, y: int) -> None:
    global is_finished
    global result

    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if maze[next_x][next_y] == 0 and cost[next_x][next_y] == -1:
                queue.append((break_wall, next_x, next_y))
                cost[next_x][next_y] = break_wall
                while queue:
                    now_break, target_x, target_y = queue.popleft()
                    if target_x == N - 1 and target_y == M - 1:
                        result = cost[N - 1][M - 1]
                        is_finished = True
                        return
                    bfs1(now_break, target_x, target_y)
            
            elif maze[next_x][next_y] == 1 and cost[next_x][next_y] == -1:
                cost[next_x][next_y] = break_wall + 1
                heapq.heappush(heap, (break_wall + 1, next_x, next_y))

queue.append((0, 0, 0))
cost[0][0] = 0

result: int = float('inf')
is_finished: bool = False
# 첫 섬의 넓이 체크
while queue:
    now_break, target_x, target_y = queue.popleft()
    if target_x == N - 1 and target_y == M - 1:
        result = cost[N - 1][M - 1]
        is_finished = True
        break
    bfs1(now_break, target_x, target_y)

# 만약 첫 섬부터 마지막이 연결됐다면?
if is_finished:
    print(f'{result}')
# 그게 아니라면
else:
    while heap:
        now_break, target_x, target_y = heapq.heappop(heap)

        if is_finished:
            break

        bfs2(now_break, target_x, target_y)
    '''
    for i in range(N):
        for j in range(M):
            print(f'{cost[i][j]}', end = ' ') if j != M - 1 else print(f'{cost[i][j]}')
    '''
    print(f'{result}')