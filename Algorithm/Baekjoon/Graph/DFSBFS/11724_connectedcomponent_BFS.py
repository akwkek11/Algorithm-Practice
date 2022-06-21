from collections import defaultdict, deque
import sys

map_dict: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))
N, M = map(int, sys.stdin.readline().strip().split())
count: int = 0
check: list = [0 for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    map_dict[start][end] = map_dict[end][start] = 1

bfs_queue = deque()
def bfs(now: int) -> None:
    for next in map_dict[now].keys():
        if check[next] == 0:
            check[next] = count
            bfs_queue.append(next)

for i in range(1, len(check)):
    if check[i] == 0:
        count += 1
        check[i] = count
        bfs_queue.append(i)
        while bfs_queue:
            next_vertex = bfs_queue.popleft()
            bfs(next_vertex)

print(count)