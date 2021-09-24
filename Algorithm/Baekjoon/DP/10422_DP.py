import math
import sys

def catalan(n: int) -> int:
    return math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    target: int = int(sys.stdin.readline().strip())
    if target % 2 == 1:
        print('0')
    else:
        print(f'{catalan(target // 2) % 1000000007}')