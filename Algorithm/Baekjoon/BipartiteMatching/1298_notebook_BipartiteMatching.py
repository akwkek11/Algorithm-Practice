from collections import defaultdict

import sys

n, m = map(int, sys.stdin.readline().strip().split())
want_map: defaultdict = defaultdict(list)
d: list = [0 for i in range(n + 1)]

def Bipartite_matching(start: int) -> int:
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in want_map[start]:
        if d[i] == 0 or Bipartite_matching(d[i]):
            d[i] = start
            return 1
    return 0

for _ in range(1, m + 1):
    people, want = map(int, sys.stdin.readline().strip().split())
    want_map[people].append(want)

for i in range(1, n + 1):
    visit = [0 for _ in range(n + 1)]
    Bipartite_matching(i)

print(len(d) - d.count(0))