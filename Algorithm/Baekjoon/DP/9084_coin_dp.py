import sys

T: int = int(sys.stdin.readline().strip())
for _ in range(T):
    N: int = int(sys.stdin.readline().strip())
    coin_list: list = list(map(int, sys.stdin.readline().strip().split()))
    target: int = int(sys.stdin.readline().strip())
    dp: list = [0 for _ in range(target + 1)]
    dp[0] = 1

    # 중복 허용 x
    for i in range(len(coin_list)):
        for j in range(coin_list[i], target + 1):
            dp[j] += dp[j - coin_list[i]]

    print(dp[target])