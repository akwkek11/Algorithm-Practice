'''
2021-08-03
'''
from itertools import permutations

# Sieve of Eratos
def prime_list(m: int, n: int, mode: int) -> list:
    '''
        Find list of prime
    '''
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
    
def solution(numbers: list) -> int:
    '''
        https://programmers.co.kr/learn/courses/30/lessons/42839
    '''
    answer: int = 0
    prime_num_list: list = prime_list(0, 9999999, 0)
    numbers_list: list = list(map(int, numbers))
    check_num: list = [0 for _ in range(10000000)]
    check_num[0] = check_num[1] = 1
    for i in range(1, len(numbers_list) + 1):
        check_list = permutations(numbers_list, i)
        for j in list(check_list):
            target: int = 0
            for k in range(len(j)):
                target += (j[k]) * (10 ** (i - 1 - k))
            if prime_num_list[target] == True and check_num[target] == 0:
                check_num[target] = 1
                answer += 1

    return answer

print(solution("1276543"))
print(solution("9999999"))
print(solution("011"))