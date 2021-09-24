import sys

def solution(temperture: list) -> list:
    stack: list = []
    result: list = [0 for _ in range(len(temperture))]

    while temperture:
        index, value = temperture.pop()
        while stack:
            prev_index, prev_value = stack.pop()
            if value > prev_value:
                result[prev_index] = index - prev_index
            else:
                stack.append((prev_index, prev_value))
                break
        stack.append((index, value))

    return result

temp_list: list = list(map(int, sys.stdin.readline().strip().split()))
res_temp_list: list = []

for i, value in enumerate(temp_list):
    res_temp_list.append((i, value))

print(f'{solution(list(reversed(res_temp_list)))}')