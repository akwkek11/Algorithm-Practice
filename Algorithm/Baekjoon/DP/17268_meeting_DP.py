import math
import sys

catalan = lambda n : math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))

target: int = int(sys.stdin.readline().strip())
if target % 2 == 1:
    print('0')
else:
    print(f'{catalan(target // 2) % 987654321}')