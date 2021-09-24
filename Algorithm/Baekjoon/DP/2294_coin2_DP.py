import sys

n, k = map(int, sys.stdin.readline().strip().split())
num_map: list = [float('inf') for _ in range(k + 1)]
num_array: list = [int(sys.stdin.readline().strip()) for _ in range(n)]
num_map[0] = 0

for i in range(n):
    for j in range(num_array[i], k + 1):
        if num_map[j - num_array[i]] != float('inf'):
            num_map[j] = min(num_map[j], num_map[j - num_array[i]] + 1)

print(f'{num_map[k]}') if num_map[k] != float('inf') else print('-1')