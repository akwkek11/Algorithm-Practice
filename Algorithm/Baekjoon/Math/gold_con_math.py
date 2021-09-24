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
        if m == 1 : m = 2
        return [i for i in range(m, n+1) if sieve[i] == True]

prime = prime_list(1,1000000,0)
prime_num = prime_list(1,1000000,1)

while True:
    cmd = sys.stdin.readline().split()
    num = int(cmd[0])
    
    i = 0
    j = len(prime)-1
    
    if num == 0: break
    else:
        while True:
            tmp = num - prime_num[i]
            if prime[tmp] == True:
                print("{0} = {1} + {2}". format(num, prime_num[i], tmp))
                break
            else :
                i = i + 1
                if prime[i] >= int(num/2):
                    print( "Goldbach's conjecture is wrong.")
                    break

        
