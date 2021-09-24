from collections import defaultdict, deque

import sys

n, k = map(int, sys.stdin.readline().strip().split())
work_map: defaultdict = defaultdict(list)
stone_num_map: list = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().strip().split())
    stone_num_map[x - 1][y - 1] = 1

col_map: list = [[0 for _ in range(n)] for _ in range(n)]
row_map: list = [[0 for _ in range(n)] for _ in range(n)]
line_num: int = 0

col_stone_num: int = 0
for j in range(n):
    for i in range(n):
        if stone_num_map[i][j] == 1 and col_map[i][j] == 0:
            col_map[i][j] = j + 1
            col_stone_num = max(col_stone_num, j + 1)
            
row_stone_num: int = 0
for i in range(n):
    for j in range(n):
        if stone_num_map[i][j] == 1 and row_map[i][j] == 0:
            row_map[i][j] = i + 1
            row_stone_num = max(row_stone_num, i + 1)

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
    for j in range(n):
        if stone_num_map[i][j] == 1:
            work_map[row_map[i][j]].append(col_map[i][j])

for i in range(1, row_stone_num + 1):
    visit: list = [0 for _ in range(row_stone_num + 1)]
    Bipartite_matching(i)

print(len(d) - d.count(0))