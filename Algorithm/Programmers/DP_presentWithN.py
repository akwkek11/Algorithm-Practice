import sys
import re

table: list = []

def solution(N, number):
    global table
    
    is_existing: bool = False
    answer: int = -1
        
    for i in range(1, 9):
        if i == 1:
            table.append([N])
        else:
            temp_list: list = []
            first_append = ''
            for j in range(0, i):
                first_append = first_append + str(N)
            temp_list.append(int(first_append))
            for k in range(0, i-1):
                for first in table[k]:
                    for second in table[(i-2)-k]:
                        temp_list.append(first+second)
                        temp_list.append(first-second)
                        temp_list.append(first*second)
                        if second:
                            temp_list.append(first//second)
            table.append(temp_list)
        if number in table[i-1]:
            is_existing = True
            answer = i
            break
    
    return answer

input_str: list = [x.strip() for x in sys.stdin.readline().strip().split(',')]
N = int(input_str[0])
number = int(input_str[1])
result = solution(N, number)

print(f'{result}')