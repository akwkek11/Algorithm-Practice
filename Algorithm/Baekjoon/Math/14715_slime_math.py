from collections import deque

import math
import sys

def prime_list(m, n, mode):
    sieve = [True for _ in range(n+1)]

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
        return [i for i in range(m, n+1) if sieve[i] == True]

prime_num: list = prime_list(1, 1000000, 0)

K: int = int(sys.stdin.readline().strip())
count: int = 1

while prime_num[K] == False:
    p = int(K ** 0.5)
    for i in range(2, p + 1):
        if K % i == 0:
            K //= i
            count += 1
            break

result: int = int(math.log2(count)) + 1 if int(math.log2(count)) < math.log2(count) else math.log2(count)
print(f'{int(result)}')
        