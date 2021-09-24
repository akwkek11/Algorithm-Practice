from bisect import bisect_left, bisect_right

import sys

N: int = int(sys.stdin.readline().strip())
num_map: list = list(map(int, sys.stdin.readline().strip().split()))
result: list = [-float('inf')]
result_count: list = []
for values in num_map:
    if result[-1] < values:
        result.append(values)
        result_count.append(len(result) - 1)

    else:
        result_index = bisect_right(result, values)
        if result_index == len(result) or result[result_index - 1] == values:
            result_index -= 1
        result[result_index] = values
        result_count.append(result_index)

target: int = max(result_count)
start: int = result_count.index(target)
print_list: list = []
print(f'{target}')
for i in range(start, -1, -1):
    if i == start or result_count[i] == target - 1:
        print_list.append(num_map[i])

        if i != start:
            target -= 1

        if target == 1:
            break

while print_list:
    print(f'{print_list.pop()}', end = ' ') if len(print_list) > 1 else print(f'{print_list.pop()}')