import sys

N, K = map(int, sys.stdin.readline().strip().split())
coin_list: list = [int(sys.stdin.readline().strip()) for _ in range(N)]
coin_list.reverse()

count: int = 0
for i in coin_list:
    if K == 0:
        break
    
    while K - i >= 0:
        K -= i
        count += 1

print(f'{count}')