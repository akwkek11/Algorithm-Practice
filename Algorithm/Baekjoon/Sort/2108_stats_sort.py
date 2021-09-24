from collections import Counter

import sys

N: int = int(sys.stdin.readline().strip())
num_list: list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline().strip()))

num_list.sort()
avg: int = int(round(sum(num_list)/len(num_list), 0))
medium: int = num_list[len(num_list) // 2]

num_count: list = [(key, value) for key, value in Counter(num_list).items()]
num_count = sorted(num_count, key=lambda x : x[1])
max_count = num_count[len(num_count) - 1][1]
res_list: list = []
mode: int = float('inf')
while num_count:
    key, value = num_count.pop()
    if value != max_count:
        break
    else:
        if mode == float('inf'):
            mode = key
        else:
            mode = res_list[len(res_list) - 1][0]
        res_list.append((key, value))

num_range: int = num_list[len(num_list) - 1] - num_list[0]

print(f'{avg}')
print(f'{medium}')
print(f'{mode}')
print(f'{num_range}')