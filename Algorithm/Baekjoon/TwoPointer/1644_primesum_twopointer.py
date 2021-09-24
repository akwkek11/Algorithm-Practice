import sys

# Sieve of Eratos
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
        if m == 1 : m = 2
        return [i for i in range(m, n+1) if sieve[i] == True]
N: int = int(sys.stdin.readline().strip())
prime_num_list: list = prime_list(2, N, 1)

list_sum: int = 0
count: int = 0
i: int = 0
j: int = 0
if N == 1:
    pass
else:
    list_sum += prime_num_list[i]

    while prime_num_list[i] < N / 2:
        while list_sum < N:
            j += 1
            list_sum += prime_num_list[j]
        
        if list_sum == N:
            count += 1
            j += 1
            list_sum += prime_num_list[j]
            if j == len(prime_num_list) - 1:
                break
        else:
            while list_sum > N:
                list_sum -= prime_num_list[i]
                i += 1
            
            if list_sum == N:
                count += 1
                list_sum -= prime_num_list[i]
                i += 1

    if N in prime_num_list:
        count += 1

print(f'{count}')