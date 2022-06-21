from collections import defaultdict, deque
import sys

bottle_dict: defaultdict = defaultdict(int)
bottle_queue: deque = deque()
bottle_queue.append((0, 0, 0))
size_a, size_b, target_a, target_b = map(int, sys.stdin.readline().strip().split())

def bfs(a: int, b: int, count: int) -> None:
    # 1. F(x)
    if not bottle_dict[(size_a, b)]:
        bottle_dict[(size_a, b)] = count
        bottle_queue.append((size_a, b, count + 1))
    
    if not bottle_dict[(a, size_b)]:
        bottle_dict[(a, size_b)] = count
        bottle_queue.append((a, size_b, count + 1))

    # 2. E(x)
    if not bottle_dict[(0, b)]:
        bottle_dict[(0, b)] = count
        bottle_queue.append((0, b, count + 1))
    
    if not bottle_dict[(a, 0)]:
        bottle_dict[(a, 0)] = count
        bottle_queue.append((a, 0, count + 1))

    # 3. M(x, y)
    now_water: int = a + b
    if now_water <= size_a:
        if not bottle_dict[(now_water, 0)]:
            bottle_dict[(now_water, 0)] = count
            bottle_queue.append((now_water, 0, count + 1))
    else:
        if not bottle_dict[(size_a, now_water - size_a)]:
            bottle_dict[(size_a, now_water - size_a)] = count
            bottle_queue.append((size_a, now_water - size_a, count + 1))

    if now_water <= size_b:
        if not bottle_dict[(0, now_water)]:
            bottle_dict[(0, now_water)] = count
            bottle_queue.append((0, now_water, count + 1))
    else:
        if not bottle_dict[(now_water - size_b, size_b)]:
            bottle_dict[(now_water - size_b, size_b)] = count
            bottle_queue.append((now_water - size_b, size_b, count + 1))

final: int = -1
while bottle_queue:
    now_a, now_b, now_count = bottle_queue.popleft()
    if (now_a, now_b) == (target_a, target_b):
        final = now_count
        break

    bfs(now_a, now_b, now_count)

print(final)