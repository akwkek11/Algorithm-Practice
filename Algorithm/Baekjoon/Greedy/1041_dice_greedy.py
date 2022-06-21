import sys

n: int = int(sys.stdin.readline().strip())
a, b, c, d, e, f = map(int, sys.stdin.readline().strip().split())
three_dice: int = min(a+b+c, a+c+e, a+d+e, a+b+d, f+b+c, f+c+e, f+d+e, f+b+d)
two_dice: int = min(a+b, a+c, a+d, a+e, b+c, b+d, b+f, e+c, e+d, e+f, c+f, d+f)
one_dice: int = min(a, b, c, d, e, f)

if n == 1:
    print(a + b + c + d + e + f - max(a, b, c, d, e, f))
else:
    some3: int = three_dice * 4
    some1: int = one_dice * (4 * (n-2) * (n-1) + (n-2) ** 2)
    some2: int = two_dice * (n**3 - (n-2) * (n-2) * (n-1) - 4 * ((n-2) * (n-1) + 1) - (n-2) ** 2)
    print(some1 + some2 + some3)