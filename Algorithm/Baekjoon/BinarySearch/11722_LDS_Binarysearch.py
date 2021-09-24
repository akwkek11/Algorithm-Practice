from bisect import bisect_right

import sys

N: int = int(sys.stdin.readline().strip())
num_list: list = list(map(int, sys.stdin.readline().strip().split()))
num_list = num_list[::-1]

result: list = [-float('inf')]
result_index: int = 0
for values in num_list:
    if result[-1] < values:
        result.append(values)
    else:
        result_index = bisect_right(result, values)
        if result_index == len(result) or result[result_index - 1] == values:
            result_index -= 1
        result[result_index] = values
    
print(f'{len(result) - 1}')