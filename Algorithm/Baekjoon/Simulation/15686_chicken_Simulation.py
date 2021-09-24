from collections import deque
from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().strip().split())
chicken_map: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
q1: deque = deque(())
q2: deque = deque(())
chicken_list: list = []

chicken_number: int = 2
home_number: int = 0
for i in range(N):
    for j in range(N):
        if chicken_map[i][j] == 1:
            q1.append((home_number, i, j))
            home_number += 1
        elif chicken_map[i][j] == 2:
            chicken_map[i][j] = chicken_number
            chicken_list.append(chicken_number)
            chicken_number += 1    

# 치킨집은 2 ~ 14로 이름 붙여주기
cost_list: list = [[0 for _ in range(len(chicken_list) + 2)] for _ in range(len(list(q1)))]
is_visited: list = [[0 for _ in range(N)] for _ in range(N)]

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

def bfs(x: int, y: int, cost: int) -> None:
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N and is_visited[next_x][next_y] == 0:
            is_visited[next_x][next_y] = 1
            q2.append((next_x, next_y, cost + 1))

def init_bfs(home_num: int, x: int, y: int) -> None:
    q2.append((x, y, 0))
    is_visited: list = [[0 for _ in range(N)] for _ in range(N)]
    is_visited[x][y] = 1
    while q2:
        target_x, target_y, now_cost = q2.popleft()
        if chicken_map[target_x][target_y] >= 2:
            cost_list[home_num][chicken_map[target_x][target_y]] = now_cost
        bfs(target_x, target_y, now_cost)

while q1:
    now_home, target_x, target_y = q1.popleft()
    init_bfs(now_home, target_x, target_y)
    for i in range(N):
        for j in range(N):
            is_visited[i][j] = 0

chicken_combination: list = list(combinations(chicken_list, M))

min_distance: int = float('inf')
now_distance: int = 0

for i in chicken_combination:
    for j in range(home_number):
        smallest_distance: int = float('inf')
        for k in i:
            smallest_distance = min(smallest_distance, cost_list[j][k])
        now_distance += smallest_distance
    min_distance = min(min_distance, now_distance)
    now_distance = 0

print(f'{min_distance}')