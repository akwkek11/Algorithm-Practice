import itertools
import sys

n: int = int(sys.stdin.readline().strip())

gcd_list: list = []
p = int(n ** 0.5)
res_value: int = n
for i in range(2, p + 1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        res_value *= (1.0 - (1.0/i))

if n > 1:
    res_value *= (1.0 - (1.0/n))

res_value = int(res_value)
print(f'{res_value}')