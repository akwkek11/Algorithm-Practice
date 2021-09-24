import sys

# C, C++, Java : -10 / 3 = -3
# Python, Ruby : -10 / 3 = -4

def DFS(start: int, value: int) -> None:
    global max_num
    global min_num
    in_value: int = value

    if start == len(num_map) or sum(num_operator) == 0:
        max_num = max(max_num, value)
        min_num = min(min_num, value)
        return

    for i in range(len(num_operator)):
        if num_operator[i] >= 1:
            if i == 0:
                in_value += num_map[start]
            elif i == 1:
                in_value -= num_map[start]
            elif i == 2:
                in_value *= num_map[start]
            elif i == 3:
                # 나눗셈의 경우, 음수면 -로 바꿔주고 몫을 챙긴 다음 다시 -
                if in_value < 0:
                    in_value = -in_value
                    in_value //= num_map[start]
                    in_value = -in_value
                else:
                    in_value //= num_map[start]
            
            num_operator[i] -= 1
            DFS(start + 1, in_value)
            num_operator[i] += 1

            in_value = value
    
    return

N: int = int(sys.stdin.readline().strip())
num_map: list = list(map(int, sys.stdin.readline().strip().split()))
num_operator: list = list(map(int, sys.stdin.readline().strip().split()))
max_num: int = -float('inf')
min_num: int = float('inf')

DFS(1, num_map[0])

print(f'{max_num}')
print(f'{min_num}')