import sys
import itertools

def sieve(n):
    is_prime = [True] * (n + 1)
    prime_list = []
    
    is_prime[0] = is_prime[1] = False
    prime_list.append(2)
    
    for i in range(3, n + 1, 2):
        if is_prime[i]: prime_list.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
    return prime_list
    
primes = sieve(40000)

def factoriaztion(n):
    ret = []
    for prime in primes:
        while n % prime == 0:
            ret.append(prime)
            n /= prime
        if n == 1: break
    if n > 1: ret.append(n)
    return ret
    
    
if __name__ == '__main__':
    n = sys.stdin.readline()
    n = int(n)
    factors = factoriaztion(n)
    print(factors)
    factors = itertools.groupby(factors)
    
    ans = 1
    
    for k, v in factors:
        l = len(list(v))
        ans = ans * (k ** l - k ** (l - 1))
    
    print(f'{ans}')