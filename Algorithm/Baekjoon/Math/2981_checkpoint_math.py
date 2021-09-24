from functools import reduce

import sys

def get_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a%b
    return a

N: int = int(sys.stdin.readline().strip())
num_list: list = [int(sys.stdin.readline().strip()) for _ in range(N)]
num_list.sort()
sub_list: list = [(num_list[i + 1] - num_list[i]) for i in range(len(num_list) - 1)]

total_gcd: int = 0
if len(sub_list) == 1:
    total_gcd = sub_list[0]
else:
    total_gcd = reduce(get_gcd, sub_list)

factorization_list: list = []
p: int = int(total_gcd ** 0.5)
for i in range(2, p + 1):
    if total_gcd % i == 0:
        factorization_list.append(i)
for i in range(len(factorization_list) - 1, -1, -1):
    next_add: int = total_gcd // factorization_list[i]
    if next_add not in factorization_list:
        factorization_list.append(next_add)

factorization_list.append(total_gcd)
string_list: list = [str(i) for i in factorization_list]
print(' '.join(string_list))