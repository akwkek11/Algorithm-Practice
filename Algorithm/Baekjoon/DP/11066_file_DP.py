# Not Solved

import sys

T: int = int(sys.stdin.readline().strip())
for _ in range(T):
    N: int = int(sys.stdin.readline().strip())
    file_size: list = list(map(int, sys.stdin.readline().strip().split()))
    file_size.insert(0, 0)
    dp: list = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    prefix: list = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + file_size[i]

    for j in range(2, N + 1):
        for i in range(j - 1, 0, -1):
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
            dp[i][j] += prefix[j] - prefix[i - 1]

    print(f'{dp[1][N]}')