import sys

N, K = map(int, sys.stdin.readline().strip().split())
zero_count: int = ((2 * N + 2 - K) ** 2) // 2 if K <= 2 * N else 0
if K % 2 == 0 and K <= 2 * N:
    zero_count += K - 1
print(f'{(2*N + 1) ** 2 - zero_count}')

'''
simulation

N: int = int(sys.stdin.readline().strip())

n_map: list = [[(i, j) for i in range(-N, N + 1)] for j in range (N, -N - 1, -1)]
is_matched: list = [[0 for _ in range(2 * N + 1)] for _ in range(2 * N + 1)]

for j in range(len(n_map)):
    for k in range(len(n_map)):
        print(f'{n_map[j][k]}', end = ' ') if k < len(n_map) - 1 else print(f'{n_map[j][k]}')

count: int = 0
for i in range(1, 2 * N + 4):
    for j in range(len(n_map)):
        for k in range(len(n_map)):
            x, y = n_map[j][k]
            if max(abs(x), abs(y)) != max(abs(x), abs(y - i)):
                is_matched[j][k] = 1
    
    print(f'check {i}')
    for j in range(len(is_matched)):
        for k in range(len(is_matched)):
            if is_matched[j][k] == 1:
                count += 1
            print(f'{is_matched[j][k]}', end = ' ') if k < len(is_matched) - 1 else print(f'{is_matched[j][k]}')
    print(count)
    print()
    count = 0
    for j in range(len(is_matched)):
        for k in range(len(is_matched)):
            is_matched[j][k] = 0
''' 