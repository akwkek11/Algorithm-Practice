from collections import deque

import sys

def gravity(n: int) -> int:
    prev_index: int = 0
    box_count: int = 0

    q: deque = deque()
    for i in range(len(box_list) - 1, -1, -1):
        if box_list[i][n] == 1:
            prev_index += len(box_list) - 1 - i
            q.append(box_list[i][n])
    
    for i in range(1, len(list(q))):
        box_count += i

    return (prev_index - box_count)

T: int = int(sys.stdin.readline().strip())
for _ in range(T):
    m, n = map(int, sys.stdin.readline().strip().split())
    box_list = [[] for _ in range(m)]

    for i in range(m):
        box_list[i] = list(map(int, sys.stdin.readline().strip().split()))

    result: int = 0
    for i in range(n):
        result += gravity(i)

    print(f'{result}')