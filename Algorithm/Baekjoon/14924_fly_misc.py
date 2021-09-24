import sys

S, T, D = map(int, sys.stdin.readline().strip().split())
print(f'{T*int(D/(S*2))}')