from collections import deque

import sys

N: int = int(sys.stdin.readline().strip())

heights: list = []
for _ in range(N):
    heights.append(int(sys.stdin.readline().strip()))

deque_heights: deque = deque(heights)
deque_heights.appendleft(0)
deque_heights.append(0)
    
heights = list(deque_heights)
check: list = [0]
max_area: int = 0
    
for i in range(1, N + 2):
    while(check and (heights[check[-1]] > heights[i])):
        cur_height = check.pop()
        max_area = max(max_area, (i - 1 - check[-1]) * heights[cur_height])
    check.append(i)
print(f'{max_area}')