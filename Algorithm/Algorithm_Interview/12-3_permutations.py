import itertools

import sys

input_num: list = list(map(int, sys.stdin.readline().strip().split()))
result: itertools = itertools.permutations(input_num, len(input_num))
final_result: list = list(map(list, result))
print(f'{final_result}')