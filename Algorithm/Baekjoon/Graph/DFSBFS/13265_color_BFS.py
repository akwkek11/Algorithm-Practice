import sys
from collections import defaultdict, deque

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    color_queue: deque = deque()
    line_dict: defaultdict = defaultdict(list)
    check: bool = True

    n, m = map(int, sys.stdin.readline().strip().split())
    color_map: list = [0 for _ in range(n + 1)]

    for i in range(m):
        start, end = map(int, sys.stdin.readline().strip().split())
        line_dict[start].append(end)
        line_dict[end].append(start)
    
    for start in range(1, n + 1):
        if color_map[start] == 0:
            color_map[start] = 1
            color_queue.append((start, color_map[start]))
            while color_queue:
                now, now_color = color_queue.popleft()
                for next in line_dict[now]:
                    if color_map[next] == 0:
                        color_map[next] = 3 - color_map[now]
                        color_queue.append((next, 3 - color_map[now]))
                    else:
                        if color_map[now] == color_map[next]:
                            check = False
                            break
        
        if not check:
            break

    if check:
        print("possible")
    else:
        print("impossible")