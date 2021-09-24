import math

a, b, c = map(int, input().split())
n = 0

c = c - a
if c == 0:
    print('1')
else:
    i, j = divmod(c, a-b)
    n = j != 0 and i+1 or i
    n = n+1
    print(str(n))
