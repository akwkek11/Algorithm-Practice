from collections import deque

import sys

N, M = map(int, sys.stdin.readline().strip().split())

circular_queue: deque = deque()
for i in range(N):
    circular_queue.append(i + 1)

pop_list: deque = deque()
for i in list(map(int, sys.stdin.readline().strip().split())):
    pop_list.append(i)

count: int = 0
while pop_list:
    target: int = pop_list.popleft()
    if circular_queue[0] == target:
        circular_queue.popleft()
    else:
        for i in range(len(circular_queue)):
            if circular_queue[i] == target:
                move: int = 0
                if i >= len(circular_queue) - i:
                    for _ in range(len(circular_queue) - i):
                        circular_queue.appendleft(circular_queue.pop())
                        count += 1
                else:
                    for _ in range(i):
                        circular_queue.append(circular_queue.popleft())
                        count += 1
                circular_queue.popleft()
                break

print(f'{count}')