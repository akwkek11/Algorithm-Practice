import sys

num_list: list = list(map(int, sys.stdin.readline().strip().split()))
stack: list = []

max_num: int = 0
while num_list:
    next_num: int = num_list.pop()
    while stack:
        stack_top: int = stack.pop()

        if not stack:
            if next_num <= stack_top:    
                stack.append(stack_top)
            break
        
        stack.append(stack_top)
        if next_num > stack[0]:
            max_num = max(max_num, max(stack) - min(stack))
            stack.clear()
        else:
            break
    stack.append(next_num)

print(f'{max(max_num, max(stack) - min(stack))}')