from bisect import bisect_left, bisect_right

import sys

N: int = int(sys.stdin.readline().strip())
num_map: list = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    num_map.append((start, end))

num_map.sort(key = lambda x : x[0])
result: list = [-float('inf')]
result_count: list = []
for key, value in num_map:
    if result[-1] < value:
        result.append(value)
        result_count.append(len(result) - 1)

    else:
        result_index = bisect_right(result, value)
        if result_index == len(result) or result[result_index - 1] == value:
            result_index -= 1
        result[result_index] = value
        result_count.append(result_index)

zero_count: int = 0
target: int = max(result_count)
start: int = result_count.index(target)
res_list: list = []

for i in range(len(result_count) - 1, start, -1):   
    res_list.append(0)
    zero_count += 1

for i in range(start, -1, -1):
    if i == start or result_count[i] == target - 1:
        res_list.append(num_map[i][1])

        if i != start:
            target -= 1

        if target == 1:
            while len(num_map) > len(res_list):   
                res_list.append(0)
                zero_count += 1
            break
    else:
        res_list.append(0)
        zero_count += 1

res_list = list(reversed(res_list))
print(f'{zero_count}')
for i in range(len(res_list)):
    if res_list[i] == 0:
        print(f'{num_map[i][0]}')