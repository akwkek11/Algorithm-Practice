from typing import List
from collections import Counter

import itertools
import re

def maximum_check(number_list: List[int], operator_list: List[str], step: List[str]) -> int:
    copy_number_list: List[int] = number_list[:]
    copy_operator_list: List[str] = operator_list[:]
    result_list: List[int] = []
    for operator in step:
        temp: int = float('inf')
        for i in range(len(copy_operator_list)):
            if copy_operator_list[i] == operator:
                if temp == float('inf'):
                    if copy_operator_list[i] == '+':
                        temp = copy_number_list[i] + copy_number_list[i + 1]
                    elif copy_operator_list[i] == '-':
                        temp = copy_number_list[i] - copy_number_list[i + 1]
                    else:
                        temp = copy_number_list[i] * copy_number_list[i + 1]
                else:
                    if copy_operator_list[i] == '+':
                        temp += copy_number_list[i + 1]
                    elif copy_operator_list[i] == '-':
                        temp -= copy_number_list[i + 1]
                    else:
                        temp *= copy_number_list[i + 1]
            else:
                if temp != float('inf'):
                    result_list.append(temp)
                    temp = float('inf')
                else:
                    result_list.append(copy_number_list[i])
        if temp != float('inf'):
            result_list.append(temp)

        while copy_operator_list.count(operator) != 0:
            copy_operator_list.remove(operator)
        if len(result_list) == len(copy_operator_list):
            result_list.append(copy_number_list[-1])
        copy_number_list = result_list[:]
        result_list.clear()

        if len(copy_number_list) == 1:
            break

    return copy_number_list[0]

def solution(expression: str):
    numbers: List[int] = [int(i) for i in re.split('[^0-9]', expression) if i]
    operators: List[str] = [i for i in re.split('[0-9]', expression) if i]
    operator_check: List[str] = list(Counter(operators).keys())
    operator_case: List[str] = itertools.permutations(operator_check, len(operator_check))
    answer: int = -float('inf')
    for i in operator_case:
        answer = max(answer, abs(maximum_check(numbers, operators, i)))
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))