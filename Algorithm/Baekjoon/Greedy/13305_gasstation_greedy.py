import sys

N: int = int(sys.stdin.readline().strip())
length: list = list(map(int, sys.stdin.readline().strip().split()))
cost: list = list(map(int, sys.stdin.readline().strip().split()))

start: int = cost[0]
go_length: int = 0
res: int = 0
for i in range(1, len(cost)):
    go_length += length[i - 1]
    if start > cost[i] or i == len(cost) - 1:
        res += start * go_length
        start = cost[i]
        go_length = 0

print(f'{res}')