import sys

dp: list = [[0 for _ in range(201)] for _ in range(201)]
for i in range(1, 201):
    dp[0][i] = 1

for i in range(1, 201):
    for j in range(1, 201):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        dp[i][j] %= 1000000000

N, K = map(int, sys.stdin.readline().strip().split())
print(f'{dp[N][K]}')