# not solved

import sys

N: int = int(sys.stdin.readline().strip())
num_map: list = list(map(int, sys.stdin.readline().strip().split()))
num_map.sort(reverse = True)
one_index: int = 0
minus_one_index: int = 0

is_one: bool = False
is_minus_one: bool = False
for i in range(N):
    if not is_one and num_map[i] == 1:
        is_one = True
    if not is_minus_one and num_map[i] == -1:
        is_minus_one = True
        one_index = i-1
        minus_one_index = i
        break

M: int = int(sys.stdin.readline().strip())
for _ in range(M):
    result: int = 0
    i, j = map(int, sys.stdin.readline().strip().split())
    if is_one and is_minus_one and i-1 <= one_index and j-1 >= minus_one_index:
        result = (min(one_index - (i - 1), (j - 1) - minus_one_index) + 1) * 2
        
    print(f'{result}')

