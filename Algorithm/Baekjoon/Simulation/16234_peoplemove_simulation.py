from collections import deque

import sys

N, L, R = map(int, sys.stdin.readline().strip().split())
q: deque = deque(())
country_map: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
is_visited: list = [[0 for _ in range(N)] for _ in range(N)]
group_check: list = [[0 for _ in range(N)] for _ in range(N)]
group_sum: list = [0 for _ in range(N * N + 1)]
group_count: list = [0 for _ in range(N * N + 1)]

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

is_possible: bool = False

def bfs(x: int, y: int, group: int) -> None:
    global is_possible
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if is_visited[next_x][next_y] == 0 and L <= abs(country_map[x][y] - country_map[next_x][next_y]) <= R:
                is_possible = True
                is_visited[next_x][next_y] = 1
                group_check[next_x][next_y] = group
                q.append((next_x, next_y, group))

move_count: int = 0
while True:
    is_possible = False
    group_number: int = 0

    # 1. 그룹 검색하기
    for i in range(N):
        for j in range(N):
            if is_visited[i][j] == 0:
                is_visited[i][j] = 1
                group_number += 1
                group_check[i][j] = group_number
                q.append((i, j, group_number))
                while q:
                    target_x, target_y, now_group = q.popleft()
                    bfs(target_x, target_y, now_group)
    
    # 만약 국경을 없앨 나라가 없다면 탈출
    if not is_possible:
        break

    # 2. 그룹별로 인구수 합산, 그룹의 수 합산
    for i in range(N):
        for j in range(N):
            group_sum[group_check[i][j]] += country_map[i][j]
            group_count[group_check[i][j]] += 1
    
    for i in range(1, N * N + 1):
        if group_count[i] != 0:
            group_sum[i] //= group_count[i]
    
    # 3. 분배
    for i in range(N):
        for j in range(N):
            country_map[i][j] = group_sum[group_check[i][j]]

    # 4. 초기화
    for i in range(N):
        for j in range(N):
            is_visited[i][j] = group_check[i][j] = 0
    for i in range(1, N * N + 1):
        group_sum[i] = group_count[i] = 0
    move_count += 1

print(f'{move_count}')