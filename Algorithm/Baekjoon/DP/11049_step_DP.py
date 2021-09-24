# Not Solved

import sys

N: int = int(sys.stdin.readline().strip())
matrix_size: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp: list = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
matrix_size.insert(0, [0, 0])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = float('inf')
        dp[i][i] = 0

for i in range(1, N):
    dp[i][i + 1] = matrix_size[i][0] * matrix_size[i][1] * matrix_size[i + 1][1]

for length in range(2, N):
    for i in range(1, N - length + 1):
        j = i + length
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + matrix_size[i][0] * matrix_size[k + 1][0] * matrix_size[j][1])

print(f'{dp[1][N]}')