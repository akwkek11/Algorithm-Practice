from collections import Counter

import math
import random
import sys
sys.setrecursionlimit(10 ** 6)

def prime_list(m, n, mode):
    sieve = [True for _ in range(n + 1)]

    p = int(n ** 0.5)
    for i in range(2, p + 1):
        if sieve[i] == True:          
            for j in range(i+i, n+1, i):
                sieve[j] = False
    # mode == 0 : return T/F Table in range
    if mode == 0:
        return sieve
    # mode == 1 : return var list in range
    elif mode == 1:
        if m == 1 : m = 3
        return [i for i in range(m, n+1) if sieve[i] == True]

prime_num_list: list = prime_list(1, 1000, 1)

# Miller-Rabin
def miller_rabin_is_prime(number: int, check_list: list) -> bool:
    odd_num: int = number - 1
    power_of_two: int = 0

    while odd_num % 2 == 0:
        power_of_two += 1
        odd_num //= 2

    for i in check_list:
        checker: int = pow(i, odd_num, number)

        if (checker == 1) or (checker == number - 1):
            continue
        try:
            for loop in range(power_of_two - 1):
                checker = pow(checker, 2, number)

                if checker == number - 1:
                    raise TypeError
        except TypeError:
            continue

        return False

    return True

# Pollard-rho
def is_prime(n: int) -> bool:
    global prime_num_list
    if n == 1 or n % 2 == 0:
        return False

    if n == 2 or n == 3:
        return True
    
    for a in prime_num_list:
        if n == a:
            return True

    if not miller_rabin_is_prime(n, prime_num_list):
        return False

    return True
def pollardRho(n: int) -> int:
    f: function = lambda x, c: (x ** 2 + c) % n

    if is_prime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2

    y = x = random.randrange(2, n)
    c: int = random.randrange(1, n)
    d: int = 1
    
    while d == 1:
        x = f(x, c)
        y = f(f(y, c), c)
        d = math.gcd(abs(x - y), n)
        if d == n:
            return pollardRho(n)

    return d if is_prime(d) else pollardRho(d)

gcd_list: list = []
n: int = int(sys.stdin.readline().strip())
while n > 1:
    div: int = pollardRho(n)
    gcd_list.append(div)
    n //= div

# 조합 경우의 수는 (각각의 소수의 지수 + 1)를 전부 곱한 것과 같다.
count: dict = dict(Counter(gcd_list))
res_value: int = 1
for key, value in count.items():
    res_value *= (value + 1)

print(f'{res_value}')