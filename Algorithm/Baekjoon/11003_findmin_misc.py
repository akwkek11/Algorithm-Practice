from collections import deque

import sys

N, L = map(int, sys.stdin.readline().strip().split())
input_num: list = list(map(int, sys.stdin.readline().strip().split()))

res = [0 for _ in range(N)]
window: deque = deque()

for i in range(N):
    while window and window[len(window)-1][1] > input_num[i]:
        window.pop()
    while window and i - window[0][0] >= L:
        window.popleft()

    window.append((i, input_num[i]))
    res[i] = window[0][1]

print(*res)

'''
N, L = map(int, sys.stdin.readline().strip().split())
num_list: list = [1000000001 for _ in range(L-1)]

input_num: list = list(map(int, sys.stdin.readline().strip().split()))
num_list.extend(input_num)

for i in range(L-1, len(num_list)):
    target_list: list = num_list[i-(L-1): i+1]
    print(f'{sorted(target_list)[0]}', end=' ')
'''