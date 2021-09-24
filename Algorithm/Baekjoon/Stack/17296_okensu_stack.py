import sys

N: int = int(sys.stdin.readline().strip())
numbers: list = list(map(int, sys.stdin.readline().strip().split()))
stack_numbers: list = []
result: list = []

while numbers:
    now_num: int = numbers.pop()
    
    while stack_numbers:
        diff_num: int = stack_numbers.pop()
        if now_num < diff_num:
            result.append(diff_num)
            stack_numbers.append(diff_num)
            stack_numbers.append(now_num)
            break

    if len(stack_numbers) == 0:
        result.append(-1)
        stack_numbers.append(now_num)

while result:
    print(f'{result.pop()}', end=' ')