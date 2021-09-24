import sys

def prime_list(m, n, mode):
    sieve = [True] * (n+1)

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

def miller_rabin_is_prime(number: int, check_list: list) -> bool:
    odd_num = number - 1
    power_of_two = 0
    while odd_num % 2 == 0:
        power_of_two += 1
        odd_num //= 2
    for i in check_list:
        checker = pow(i,odd_num, number)
        if (checker == 1) or (checker == number - 1):
            continue
        try:
            for loop in range(power_of_two - 1):
                checker = pow(checker,2,number)
                if checker == number - 1:
                    raise TypeError
        except TypeError:
            continue
        return False
    return True

n: int = int(sys.stdin.readline().strip())
size_list: list = [0 for _ in range(n)]
result: int = 0
prime: list = prime_list(1,1000000,0)
prime_num_list = prime_list(1, 70, 1)

for i in range(n):
    size_list[i] = int(sys.stdin.readline().strip())

for i in size_list:
    if 2*i + 1 <= 1000000:
        if prime[2*i+1]:
            result += 1
    else:
        if miller_rabin_is_prime(i*2+1, prime_num_list):
            result += 1

print(f'{result}')