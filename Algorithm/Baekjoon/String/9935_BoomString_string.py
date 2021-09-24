import sys

original: list = list(str(sys.stdin.readline().strip()))
target: str = str(sys.stdin.readline().strip())
stack: list = []
detection: str = target[::-1]
detection_index_list: list = [0]

while original:
    next_str = original.pop()
    next_index = detection_index_list[-1]
    stack.append(next_str)
    if next_str == detection[next_index]:
        if next_index == len(target) - 1:
            detection_index_list.append(next_index + 1)
            for _ in range(len(target)):
                stack.pop()
                detection_index_list.pop()
        else:
            detection_index_list.append(next_index + 1)
    else:
        detection_index_list.append(1) if next_str == detection[0] else detection_index_list.append(0)

result: str = ''.join(list(reversed(stack)))
print(f'{result}') if len(result) != 0 else print('FRULA')