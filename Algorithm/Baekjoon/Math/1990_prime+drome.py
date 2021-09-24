import sys

def prime_list(m: int, n: int, mode: int) -> list:
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
        if m == 1 : 
            m = 2
        ret_list: list = [i for i in range(m, n+1) if sieve[i] == True]
        return [i for i in ret_list if str(i) == str(i)[::-1]]

a, b = map(int, sys.stdin.readline().strip().split())

res_list1: list = []
res_list2: list = []
if b < 100000:
    res_list1 = prime_list(a, b, 1)
else:
    if a < 100000:
        res_list1 = prime_list(a, 100000, 1)

    if b >= 1000000:
        if a >= 10000000:
            pass
        else:
            res_list2 = prime_list(max(1000000, a), min(10000000, b), 1)

for i in res_list1:
    print(f'{i}')

for i in res_list2:
    print(f'{i}')
print('-1')