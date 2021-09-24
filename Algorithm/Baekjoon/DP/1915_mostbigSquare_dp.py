import sys

N, M = map(int, sys.stdin.readline().strip().split())
res_map: list = [[0 for _ in range(M)] for _ in range(N)]

zero_one_map: list = []

for _ in range(N):
    zero_one_map.append(list(str(sys.stdin.readline().strip())))

max_num: int = 0 
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            if zero_one_map[i][j] == '1':
                res_map[i][j] = 1
        else:
            if zero_one_map[i][j] == '1':
                res_map[i][j] = min(res_map[i-1][j-1], res_map[i-1][j], res_map[i][j-1]) + 1
        
        if res_map[i][j] > max_num:
            max_num = res_map[i][j]

print(f'{max_num ** 2}')