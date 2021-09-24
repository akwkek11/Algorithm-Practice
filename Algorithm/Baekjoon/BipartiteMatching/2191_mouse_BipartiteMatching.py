from collections import defaultdict

import sys

n, m, s, v = map(int, sys.stdin.readline().strip().split())
safe_map: defaultdict = defaultdict(list)
d: list = [0 for _ in range(m + 1)]

def Bipartite_matching(start: int) -> int:
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in safe_map[start]:
        if d[i] == 0 or Bipartite_matching(d[i]):
            d[i] = start
            return 1
    return 0

mouse_info: list = [(float('inf'), float('inf'))]
for i in range(n):
    mouse_x, mouse_y = map(float, sys.stdin.readline().strip().split())
    mouse_info.append((mouse_x, mouse_y))

for i in range(1, m + 1):
    target_x, target_y = map(float, sys.stdin.readline().strip().split())
    for index, value in enumerate(mouse_info):
        if ((target_x - value[0]) ** 2 + (target_y - value[1]) ** 2) ** 0.5 <= float(s * v):
            safe_map[index].append(i)

for i in range(1, n + 1):
    visit: list = [0 for _ in range(n + 1)]
    Bipartite_matching(i)

print(n - (len(d) - d.count(0)))