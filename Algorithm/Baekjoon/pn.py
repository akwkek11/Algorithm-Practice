def prime_list(m, n):
    sieve = [True] * (n+1)

    p = int(n ** 0.5)
    for i in range(2, p + 1):
        if sieve[i] == True:          
            for j in range(i+i, n+1, i):
                sieve[j] = False
    if m == 1 : m = 2
    return [i for i in range(m, n+1) if sieve[i] == True]

a, b = map(int, input().split())

for i in prime_list(a,b):
    print(i)
