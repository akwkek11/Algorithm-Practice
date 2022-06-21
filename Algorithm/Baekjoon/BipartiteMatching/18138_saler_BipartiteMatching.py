from collections import defaultdict

import sys

n, m = map(int, sys.stdin.readline().strip().split())
cloth_map: defaultdict = defaultdict(list)
d: list = [0 for _ in range(m + 1)]

def Bipartite_matching(start: int) -> int:
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in cloth_map[start]:
        if d[i] == 0 or Bipartite_matching(d[i]):
            d[i] = start
            return 1
    return 0

cloth_size: list = [0]
for _ in range(1, n + 1):
    cloth_size.append(int(sys.stdin.readline().strip()))

for i in range(1, m + 1):
    kara: int = int(sys.stdin.readline().strip())
    for j in range(1, n + 1):
        if cloth_size[j] / 2 <= kara <= (cloth_size[j] * 3) / 4 or cloth_size[j] <= kara <= (cloth_size[j] * 5) / 4:
            cloth_map[j].append(i)

for i in range(1, n + 1):
    visit = [0 for _ in range(n + 1)]
    Bipartite_matching(i)

print(d)
print(len(d) - d.count(0))