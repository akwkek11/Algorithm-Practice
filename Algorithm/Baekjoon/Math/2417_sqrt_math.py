import sys

n: int = int(sys.stdin.readline().strip())
target: int = int(n ** 0.5)
if target ** 2 < n:
    target += 1
print(target)