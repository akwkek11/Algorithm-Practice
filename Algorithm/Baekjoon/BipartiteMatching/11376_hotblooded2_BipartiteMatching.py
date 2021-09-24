from collections import defaultdict

import sys
sys.setrecursionlimit(10 ** 5)

n, m = map(int, sys.stdin.readline().strip().split())
work_map: defaultdict = defaultdict(lambda : defaultdict(list))
d: list = [0 for i in range(m + 1)]

def Bipartite_matching(start: int, index: int) -> int:
    if visit[start][index] == 1:
        return 0
    visit[start][index] = 1
    for i in range(2):
        for j in work_map[start][i]:
            if d[j] == 0 or Bipartite_matching(d[j], i):
                d[j] = start
                return 1
    return 0

for i in range(1, n + 1):
    num, *want = map(int, sys.stdin.readline().strip().split())
    for j in range(2):
        for k in want:
            work_map[i][j].append(k)

for i in range(1, n + 1):
    for j in range(2):
        visit = [[0 for _ in range(2)] for _ in range(n + 1)]
        Bipartite_matching(i, j)

print(len(d) - d.count(0))