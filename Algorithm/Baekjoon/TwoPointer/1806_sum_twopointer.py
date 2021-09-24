import sys

N, S = map(int, sys.stdin.readline().strip().split())
num_map: list = list(map(int, sys.stdin.readline().strip().split()))

# Two pointer
i: int = 0
j: int = 0
min_len: int = float('inf')
list_sum: int = num_map[0]
while i < N and j < N:
    if list_sum >= S:
        min_len = min(min_len, j - i + 1)
        list_sum -= num_map[i]
        i += 1
    else:
        j += 1
        list_sum += num_map[j] if j < N else 0
        
print(f'{min_len}') if min_len != float('inf') else print('0')