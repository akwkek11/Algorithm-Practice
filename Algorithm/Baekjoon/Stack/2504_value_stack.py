import sys

input_string: str = sys.stdin.readline().strip()
input_list: list = list(input_string)
start_stack: list = []
already_search: list = [0 for i in range(31)]
error: bool = False
answer: int = 0

def recursive_function(input_list: list, i: int) -> int:
    sub_value = 1
    global start_stack
    global already_search
    global error

    already_search[i] = 1
    last_index = 0

    if input_list[i] == '(' or input_list[i] == '[':
        start_stack.append(input_list[i])
        
        if i + 1 == len(input_list):
            error = True
            return 0

        else:
            for j in range(i+1, len(input_list)):
                if not already_search[j]:
                    if input_list[j] == '(' or input_list[j] == '[':
                        if sub_value == 1:
                            sub_value = 0
                        sub_value += recursive_function(input_list, j)
                    else:
                        last_index = j
                        already_search[j] = 1
                        break
    
    if len(start_stack) == 0:
        error = True
        return 0

    val = start_stack.pop()
    if input_list[last_index] == ')' and val == '(':
        return sub_value * 2
    elif input_list[last_index] == ']' and val == '[':
        return sub_value * 3
    else:
        error = True
        return 0

for i in range(len(input_list)):
    if len(input_list)%2 or error:
        answer = 0
        break
        
    if not already_search[i]:
        answer += recursive_function(input_list, i)

print(answer)