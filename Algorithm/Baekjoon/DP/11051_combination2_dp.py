import sys

dp: list =[[0 for _ in range(1001)] for _ in range(1001)]
division: int = 10 ** 4 + 7

dp[1][1] = dp[1][0] = dp[0][0] = 1
for i in range(2, 1001):
    for j in range(i + 1):
        if j in [0, i]:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp[i][j] %= division

N, K = map(int, sys.stdin.readline().strip().split())
print(f'{dp[N][K]}')