from collections import Counter

import sys

N: int = int(sys.stdin.readline().strip())
num_dict: list = [0 for _ in range(10001)]
for _ in range(N):
    num_dict[int(sys.stdin.readline())] += 1

res_str: list = []
for i in range(1, len(num_dict)):
    for j in range(num_dict[i]):
        res_str.append(str(i))
        res_str.append('\n')
        if len(res_str) >= 10000:
            print(''.join(res_str), end='')
            res_str.clear()

if len(res_str):
    res_str.pop()
    print(''.join(res_str))