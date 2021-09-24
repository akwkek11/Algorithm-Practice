from collections import deque

import sys

N: int = int(sys.stdin.readline().strip())
q: deque = deque()
result: list = []
for _ in range(N):
    q.append(str(sys.stdin.readline().strip()))

i: int = 0
j: int = N - 1

def compare(x: int, y: int) -> bool:
    compare_list: list = list(q)
    while len(compare_list) > 1 and x < len(compare_list) and y >= 0 and compare_list[x] == compare_list[y] and x < y:
        x += 1
        y -= 1
    return (compare_list[x] <= compare_list[y])

count: int = 0
while q:
    check: bool = compare(i, j)
    result.append(q.popleft()) if check else result.append(q.pop())
    j -= 1
    count += 1
    if count == 80:
        result.append('\n')
        count = 0

print(''.join(result))