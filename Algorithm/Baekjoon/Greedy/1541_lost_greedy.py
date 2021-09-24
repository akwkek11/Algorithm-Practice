import re
import sys

input_str: str = str(sys.stdin.readline().strip())
operators: list = [i for i in input_str if i == '+' or i == '-']
num_list: list = list(map(int, re.split('[-+]', input_str)))

index: int = 0
first_minus: int = -1
sum_list: list = []
while index < len(operators):
    if operators[index] == '-':
        if first_minus == -1:
            first_minus = index

        temp_sum: int = 0
        for i in range(index + 1, len(num_list)):
            index += 1
            if index == len(operators) or operators[index] == '-':
                index -= 1
                sum_list.append(temp_sum + num_list[i])
                break
            else:
                temp_sum += num_list[i]
    
    index += 1

result: int = 0
if first_minus == -1:
    result = sum(num_list)
else:
    for i in range(0, first_minus + 1):
        result += num_list[i]
    result -= sum(sum_list)
print(f'{result}')