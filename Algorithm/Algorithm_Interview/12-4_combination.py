import itertools

import sys

n, k = map(int, sys.stdin.readline().strip().split())
input_num: list = [i for i in range(1, n + 1)]
result: itertools = itertools.combinations(input_num, k)
final_result: list = list(map(list, result))
print(f'{final_result}')