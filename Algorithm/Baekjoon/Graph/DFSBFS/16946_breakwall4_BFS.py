from collections import deque

import sys

N, M = map(int, sys.stdin.readline().strip().split())
maze_map: list = [list(map(int, list(str(sys.stdin.readline().strip())))) for _ in range(N)]
is_visited: list = [[0 for _ in range(M)] for _ in range(N)]
zero_number_list: list = [[0 for _ in range(M)] for _ in range(N)]
zero_sum_list: list = [[0 for _ in range(M)] for _ in range(N)]
zero_number: int = 0
count: int = 0

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

def BFS(x: int, y: int) -> None:
    global count

    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M and is_visited[next_x][next_y] == 0 and maze_map[next_x][next_y] == 0:
            is_visited[next_x][next_y] = 1
            q.append((next_x, next_y))
            fill.append((next_x, next_y))

q: deque = deque(())
fill: deque = deque(())
for i in range(N):
    for j in range(M):
        if maze_map[i][j] == 0 and is_visited[i][j] == 0:
            zero_number += 1
            is_visited[i][j] = 1
            q.append((i, j))
            fill.append((i, j))
            while q:
                target_x, target_y = q.popleft()
                count += 1
                zero_number_list[target_x][target_y] = zero_number
                BFS(target_x, target_y)
            while fill:
                target_x, target_y = fill.popleft()
                zero_sum_list[target_x][target_y] = count

            count = 0
'''
for i in range(N):
    for j in range(M):
        print(zero_sum_list[i][j], end = '') if j != M - 1 else print(zero_sum_list[i][j])
print()
for i in range(N):
    for j in range(M):
        print(zero_number_list[i][j], end = '') if j != M - 1 else print(zero_number_list[i][j])
print()
'''
for i in range(N):
    for j in range(M):
        if maze_map[i][j] == 1:
            temp: int = 1
            sum_list: list = []
            if i - 1 >= 0 and maze_map[i - 1][j] == 0:
                temp += zero_sum_list[i - 1][j] % 10
                sum_list.append(zero_number_list[i - 1][j])
            
            if i + 1 < N and maze_map[i + 1][j] == 0:
                if zero_number_list[i + 1][j] not in sum_list:
                    temp += zero_sum_list[i + 1][j] % 10
                    sum_list.append(zero_number_list[i + 1][j])

            if j - 1 >= 0 and maze_map[i][j - 1] == 0:
                if zero_number_list[i][j - 1] not in sum_list:
                    temp += zero_sum_list[i][j - 1] % 10
                    sum_list.append(zero_number_list[i][j - 1])

            if j + 1 < M and maze_map[i][j + 1] == 0:
                if zero_number_list[i][j + 1] not in sum_list:
                    temp += zero_sum_list[i][j + 1] % 10
            
            temp %= 10
            maze_map[i][j] = temp

for i in range(N):
    for j in range(M):
        print(f'{maze_map[i][j]}', end='') if j != M - 1 else print(f'{maze_map[i][j]}')