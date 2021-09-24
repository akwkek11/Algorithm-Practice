import sys

N: int = int(sys.stdin.readline().strip())
boj_str: str = str(sys.stdin.readline().strip())
dp: list = [float('inf') for _ in range(N + 1)]
dp[0] = 0
if len(boj_str) == 1:
    print(dp[0])
else:
    try:
        start_O: int = boj_str.index('O')
        for i in range(N):
            if boj_str[i] == 'B':
                if i == 0 or i > start_O:
                    for j in range(i + 1, N):
                        if boj_str[j] == 'O':
                            dp[j] = min(dp[j], dp[i] + (i - j) ** 2)
            
            elif boj_str[i] == 'O':
                for j in range(i + 1, N):
                    if boj_str[j] == 'J':
                        dp[j] = min(dp[j], dp[i] + (i - j) ** 2)
            
            elif boj_str[i] == 'J':
                for j in range(i + 1, N):
                    if boj_str[j] == 'B':
                        dp[j] = min(dp[j], dp[i] + (i - j) ** 2)

        print(f'{dp[N - 1]}') if dp[N - 1] != float('inf') else print('-1')
    except ValueError:
        print('-1')