import sys

n, k = map(int, sys.stdin.readline().strip().split())
coin_list: list = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp1: list = [0 for _ in range(k + 1)]
dp2: list = [0 for _ in range(k + 1)]
dp1[0] = 1
dp2[0] = 1

# 중복 허용 x
for i in range(n):
    for j in range(coin_list[i], k + 1):
        dp1[j] += dp1[j - coin_list[i]]

print(dp1)

# 중복 허용 o

for i in range(k + 1):
    for j in range(n):
        if i - coin_list[j] >= 0:
            dp2[i] += dp2[i - coin_list[j]]

print(dp2)