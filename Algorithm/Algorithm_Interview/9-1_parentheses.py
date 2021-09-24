import sys

s: str = str(sys.stdin.readline().strip())
list_s: list = list(s)

stack: list = []
while list_s:
    next_str: str = list_s.pop()
    if next_str in [']', ')', '}']:
        stack.append(next_str)
    else:
        is_vaild = stack.pop()
        if [next_str, is_vaild] not in [['[', ']'], ['(', ')'], ['{', '}']]:
            break

print(f'{not stack and not list_s}')