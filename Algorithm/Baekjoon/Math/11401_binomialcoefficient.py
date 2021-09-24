import sys

p: int = 1000000007
N, K = map(int, sys.stdin.readline().strip().split())

num_N: int = 1
for i in range(1, N + 1):
    num_N *= i
    num_N %= p

num_K: int = 1
for i in range(1, K + 1):
    num_K *= i
    num_K %= p
for i in range(1, N - K + 1):
    num_K *= i
    num_K %= p

cycle: int = p - 2
A: int = num_N
B: int = num_K
C: int = 1 
while cycle > 0:
    if cycle % 2 == 1:
        C *= B
        C %= p
    B *= B
    B %= p
    cycle //= 2

res: int = (A * C) % p
print(f'{res}')