from collections import defaultdict

import sys

n, m = map(int, sys.stdin.readline().strip().split())
cow_map: defaultdict = defaultdict(list)
d: list = [0 for i in range(m + 1)]

def Bipartite_matching(start: int) -> int:
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in cow_map[start]:
        if d[i] == 0 or Bipartite_matching(d[i]):
            d[i] = start
            return 1
    return 0

for i in range(1, n + 1):
    num, *want = map(int, sys.stdin.readline().strip().split())
    for j in want:
        cow_map[i].append(j)

for i in range(1, n + 1):
    visit = [0 for _ in range(n + 1)]
    Bipartite_matching(i)

print(len(d) - d.count(0))