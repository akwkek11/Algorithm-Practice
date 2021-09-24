import sys

'''
def concatenation(numbers):
    return ''.join([i for i in numbers])

def solution(numbers):
    answer: str = ''
    temp_answer: list = ['' for i in range(10)]

    temp: list = []
    temp = sorted(map(str, numbers))
    temp.sort(key=lambda x : x[min(1, len(x)-1)])
    temp.reverse()

    result: list = [[] for i in range(10)]
    is_all_zero: bool = True

    for i in range(len(result)):
        for j in temp:
            if j[0] == str(i):
                result[i].append(j)
                if i >= 1 and is_all_zero:
                    is_all_zero = False

    for i in range(1, len(result)):
        for j in range(len(result[i])-1):
            if len(result[i][j]) >= 2 and len(result[i][j+1]) >= 2:
                if result[i][j][0] == result[i][j+1][0] and result[i][j][1] == result[i][j+1][1]:
                    if int(result[i][j][2*len(result[i][j])-4]) < int(result[i][j+1][2*len(result[i][j+1])-4]):
                        sort_temp: str = result[i][j+1]
                        result[i][j+1] = result[i][j]
                        result[i][j] = sort_temp
                    elif int(result[i][j][2*len(result[i][j])-4]) == int(result[i][j+1][2*len(result[i][j+1])-4]) and len(result[i][j]) > len(result[i][j+1]):

    for i in range(len(result[1])):
        if int(result[1][i]) == 1000:
            thousand = result[1].pop(i)
            result[1].append(thousand)
    
    if is_all_zero:
        return '0'
    
    else:
        for i in range(len(temp_answer)):
            temp_answer[i] = concatenation(result[i])
        temp_answer.reverse()
        answer = concatenation(temp_answer)
        return answer
'''
def solution(numbers):
    size = len(str(max(numbers))) + 1

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*size, reverse=True) 
    
    return ''.join(numbers) if numbers[0] != '0' else '0'

numbers = list(map(int, sys.stdin.readline().strip().split()))
print(solution(numbers))