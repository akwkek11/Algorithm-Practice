import sys

N: int = int(sys.stdin.readline().strip())
num_map: list = list(map(int, sys.stdin.readline().strip().split()))
num_map.sort()

# Two pointer
i: int = 0
j: int = N - 1

# result values
min_distance: int = float('inf')
save_i: int = 0
save_j: int = 0

while j - i > 0:
    distance: int = num_map[j] + num_map[i]
    if min_distance > abs(distance):
        min_distance = abs(distance)
        save_i = num_map[i]
        save_j = num_map[j]

    if distance > 0:
        j -= 1
    else:
        i += 1

print(f'{save_i} {save_j}')