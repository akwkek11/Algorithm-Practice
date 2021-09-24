import sys

def solution(money):
    answer: int = 0
    max_money1: list = [0 for _ in range(len(money))]
    max_money2: list = [0 for _ in range(len(money))]

    for i in range(len(money)-1):
        if i == 0:
            max_money1[i] = money[i]
        elif i == 1:
            max_money1[i] = max(max_money1[0], money[1])
        else:
            max_money1[i] = max(max_money1[i-2] + money[i], max_money1[i-1])

    for i in range(len(money)):
        if i == 0:
            max_money2[0] = 0
        elif i == 1:
            max_money2[i] = max(max_money2[0], money[1])
        else:
            max_money2[i] = max(max_money2[i-2] + money[i], max_money2[i-1])
    
    answer = max(max_money1[len(money)-2], max_money2[len(money)-1])
    return answer

house_list: list = list(map(int, sys.stdin.readline().strip().split()))
res: int = solution(house_list)
print(f'{res}')