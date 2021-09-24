from collections import defaultdict, deque

import sys

n, m = map(int, sys.stdin.readline().strip().split())
work_map: defaultdict = defaultdict(list)
stone_map: list = [str(sys.stdin.readline().strip()) for _ in range(n)]
stone_num_map: list = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        stone_num_map[i][j] = 1 if stone_map[i][j] == '*' else 0

q: deque = deque(())
col_map: list = [[0 for _ in range(m)] for _ in range(n)]
row_map: list = [[0 for _ in range(m)] for _ in range(n)]
line_num: int = 0

def bfs(x: int, y: int, direction: int) -> None:
    if direction == 0:
        next_x = x + 1
        if 0 <= next_x < n and col_map[next_x][y] == 0 and stone_num_map[next_x][y] == 1:
            col_map[next_x][y] = line_num
            q.append((next_x, y))
    else:
        next_y = y + 1
        if 0 <= next_y < m and row_map[x][next_y] == 0 and stone_num_map[x][next_y] == 1:
            row_map[x][next_y] = line_num
            q.append((x, next_y))

# 0 = x, 1 = y
direction_xy: int = 0
for j in range(m):
    for i in range(n):
        if stone_num_map[i][j] == 1 and col_map[i][j] == 0:
            line_num += 1
            q.append((i, j))
            col_map[i][j] = line_num
            while q:
                target_x, target_y = q.popleft()
                bfs(target_x, target_y, direction_xy)

col_stone_num: int = line_num
direction_xy = 1
line_num = 0
for i in range(n):
    for j in range(m):
        if stone_num_map[i][j] == 1 and row_map[i][j] == 0:
            line_num += 1
            q.append((i, j))
            row_map[i][j] = line_num
            while q:
                target_x, target_y = q.popleft()
                bfs(target_x, target_y, direction_xy)

row_stone_num: int = line_num
d: list = [0 for i in range(col_stone_num + 1)]

def Bipartite_matching(start: int) -> int:
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in work_map[start]:
        if d[i] == 0 or Bipartite_matching(d[i]):
            d[i] = start
            return 1
    return 0

for i in range(n):
    for j in range(m):
        if stone_num_map[i][j] == 1:
            work_map[row_map[i][j]].append(col_map[i][j])

for i in range(1, row_stone_num + 1):
    visit: list = [0 for _ in range(row_stone_num + 1)]
    Bipartite_matching(i)

print(len(d) - d.count(0))