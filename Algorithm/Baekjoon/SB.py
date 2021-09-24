import math

a, b, c = map(int, input().split())

n = 0
if c - b <= 0:
    print('-1')
else:
    i, j = divmod(a, c-b)
    n = i+1
    print(str(n))
