import sys

# Sieve of Eratos
def prime_list(m: int, n: int, mode: int) -> list:
    sieve: list = [True for _ in range(n + 1)] 

    p: int = int(n ** 0.5)
    for i in range(2, p + 1):
        if sieve[i] == True:          
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    # mode == 0 : return T/F Table in range
    if mode == 0:
        return sieve
    # mode == 1 : return var list in range
    elif mode == 1:
        if m == 1 : m = 2
        return [i for i in range(m, n + 1) if sieve[i] == True]

prime_list: list = prime_list(1, 1000000, 0)

M: int = int(sys.stdin.readline().strip())

a: int = M // 3 if M % 3 == 0 else M // 3 + 1

b: int = 0
if prime_list[M] == True:
    b = 1
else:
    count_two: int = 0
    while prime_list[M] == False:
        p: int = int(M ** 0.5)
        for i in range(2, p + 1):
            if M % i == 0:
                if i == 2:
                    count_two += 1

                M //= i
                b += 1

                if count_two == 2:
                    b -= 1
                    count_two = 0

                break

    if M != 1:
        if not (M == 2 and count_two == 1):
            b += 1
    
print(a, b)