from collections import defaultdict, deque
import sys

map_dict: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))
N, M, K, X = map(int, sys.stdin.readline().strip().split())
bfs_queue: deque = deque()
bfs_queue.append((X, K))
check: list = [0 for _ in range(N + 1)]
check[X] = 1
result: list = []

def bfs(now: int, count: int) -> None:
    for next in map_dict[now].keys():
        if check[next] == 0:
            check[next] = 1
            if count > 1:
                bfs_queue.append((next, count - 1))
            else:
                result.append(next)

for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    map_dict[start][end] = 1

while bfs_queue:
    now_city, now_step = bfs_queue.popleft()
    bfs(now_city, now_step)

result.sort()
if len(result) == 0:
    print(-1)
else:
    for cities in result:
        print(cities)