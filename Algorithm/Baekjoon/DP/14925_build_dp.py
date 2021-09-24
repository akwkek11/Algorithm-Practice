import sys

M, N = map(int, sys.stdin.readline().strip().split())
field: list = [[0] for _ in range(M+1)]
size: list = [[0 for _ in range(N+1)] for _ in range(M+1)]

field[0].extend([0 for _ in range(N)])
for i in range(1, M+1):
    field[i].extend(list(map(int, sys.stdin.readline().strip().split())))

max_size: int = 0
for i in range(1, M+1):
    for j in range(1, N+1):
        if field[i][j] == 0:
            size[i][j] = min(size[i-1][j], size[i][j-1], size[i-1][j-1]) + 1
            max_size = max(max_size, size[i][j])

print(f'{max_size}')