import sys

N: int = int(sys.stdin.readline().strip())
num_map: list = [float('inf') for _ in range(max(4, N + 1))]
num_map[0] = num_map[1] = 0
num_map[2] = num_map[3] = 1

for i in range(4, N + 1):
    chk: list = []
    chk.append(num_map[i - 1])
    if i % 2 == 0:
        chk.append(num_map[i // 2])
    if i % 3 == 0:
        chk.append(num_map[i // 3])
    num_map[i] = min(chk) + 1

res_stack: list = []
def backtrack(i: int) -> bool:
    if i == 1:
        res_stack.append(i)
        return True

    if i % 2 == 0 and num_map[i] - 1 == num_map[i // 2]:
        if backtrack(i // 2):
            res_stack.append(i)
            return True
    
    if i % 3 == 0 and num_map[i] - 1 == num_map[i // 3]:
        if backtrack(i // 3):
            res_stack.append(i)
            return True

    if i - 1 >= 1 and num_map[i] - 1 == num_map[i - 1]:
        if backtrack(i - 1):
            res_stack.append(i)
            return True

    return False
print(f'{num_map[N]}')
backtrack(N)
while res_stack:
    print_value: int = res_stack.pop()
    print(f'{print_value}', end = ' ') if res_stack else print(f'{print_value}')