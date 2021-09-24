from collections import Counter

import itertools
import math
import random
import sys

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

prime_num_list: list = prime_list(1, 50, 1)
# check_list = [2, 7, 61, 325, 9375, 28178, 450775, 9780504, 1795265022]

# Miller-Rabin
def miller_rabin_is_prime(number: int, check_list: list) -> bool:    
    if number < 5 or number & 1 == 0 or number % 3 == 0:
        return 2 <= number <= 3
    s: int = ((n - 1) & (1 - n)).bit_length() - 1
    d: int = n >> s

    for i in check_list:
        checker: int = pow(i, d, number)

        if (checker == 1) or (checker == number - 1) or i % number == 0:
            continue
        
        for _ in range(s):
            checker = pow(checker, 2, number)
                
            if checker == number - 1:
                break
        else:
            return False

    return True

# Pollard-rho
def is_prime(n: int) -> bool:
    global prime_num_list
    check_list: list = [2, 7, 61, 325, 9375, 28178, 450775, 9780504, 1795265022]
    if n == 1 or n % 2 == 0:
        return False

    if n == 2 or n == 3:
        return True
    
    for a in prime_num_list:
        if n == a:
            return True

    if not miller_rabin_is_prime(n, check_list):
        return False

    return True

gcd_list: list = []
n: int = int(sys.stdin.readline().strip())
f = lambda x, c: (x ** 2 + c) % n 

if n < 10 ** 12:
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

else:
    while n > 1:
        for p in prime_num_list:
            while n % p == 0:
                n //= p
                gcd_list.append(p)

        if n == 1:
            break

        if is_prime(n):
            gcd_list.append(n)
            break
        
        while True:
            y = x = random.randrange(2, n)
            c: int = random.randrange(1, n)
            d: int = 1
            
            while d == 1:
                x = f(x, c)
                y = f(f(y, c), c)
                d = math.gcd(abs(x - y), n)
                if d == n:
                    continue
            
            if is_prime(d):
                gcd_list.append(d)
                n //= d
                continue
            
            else:
                n = d
                continue

    factors = itertools.groupby(gcd_list)
    res_value: int = 1

    # 오일러 피 함수
    for k, v in factors:
        l: int = len(list(v))
        res_value *= (k ** l - k ** (l - 1))

    print(f'{res_value}')