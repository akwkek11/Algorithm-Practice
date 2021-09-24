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

N: int = int(sys.stdin.readline().strip())
res_list: list = prime_list(N, 1100000, 1)

print(f'{res_list[0]}')