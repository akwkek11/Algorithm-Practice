import sys

N: int = int(sys.stdin.readline().strip())
xy_list: list = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
xy_list = xy_list[::-1]
xy_list.append(xy_list[0])

sum_1: int = 0
sum_2: int = 0
for i in range(N):
    sum_1 += xy_list[i][0] * xy_list[i + 1][1]
    sum_2 += xy_list[i][1] * xy_list[i + 1][0]

print(f'{abs(round((sum_1 - sum_2) / 2, 1))}')