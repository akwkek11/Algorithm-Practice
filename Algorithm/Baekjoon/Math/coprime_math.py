import sys
import itertools

def coprime_list(n: int) -> list:
    target: int = int((n+1) ** 0.5)
    sieve: list = [True for i in range(target + 1)]
    result: list = []
    last_num: int = n

    for i in range(2, target + 1):
        if n%i == 0 and sieve[i] == True:
            result.append(i)          
            for j in range(i + i, target + 1, i):
                sieve[j] = False

    for i in result:
        while True:
            last_num = last_num//i
            if last_num%i != 0:
                break
    
    if last_num != 1:
        result.append(last_num)

    return result

T: int = int(input())
answer: int = 0

for count in range(1, T + 1):
    A, B, N = map(int, sys.stdin.readline().strip().split())
    coprime: list = coprime_list(N)
    answer: int = B-A+1
    temp_list: list = []
    final_list: list = []
    final_list.append(coprime)

    if len(coprime) != 1:
        temp_num: int = 1
        for i in range(2, len(coprime)+1):
            combination_list = list(itertools.combinations(coprime, i))
            for j in range(len(combination_list)):
                for k in combination_list[j]:
                    temp_num *= k
                temp_list.append(temp_num)
                temp_num = 1
            final_list.append(temp_list)
            temp_list = []

    if N == 1:
        pass
    else :
        for i in range(len(final_list)):
            for j in final_list[i]:
                answer += ((B//j) - ((A-1)//j))*((2*(i%2))-1)
    
    print(f"Case #{count}: {answer}")