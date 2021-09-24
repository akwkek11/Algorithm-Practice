import sys

res_map: list = [0 for _ in range(1000 + 1)]

res_map[1] = 1 # SK
res_map[2] = 0 # CY
res_map[3] = 1 # SK
res_map[4] = 1 # SK
res_map[5] = 1 # SK

for i in range(6, len(res_map)):
    is_win: bool = False
    for j in [1, 3, 4]:
        check_value = res_map[i - j]
        if check_value == 0:
            is_win = True
            break
    
    res_map[i] = 1 if is_win else 0

N: int = int(sys.stdin.readline().strip())

print('SK') if res_map[N] else print('CY')