import itertools

import sys

input_num: list = list(map(int, sys.stdin.readline().strip().split()))
final_result: list = []
for i in range(0, len(input_num) + 1):
    result: itertools = itertools.combinations(input_num, i)
    for j in list(map(list, result)):
        final_result.append(j)

print(f'{final_result}')