import sys

N, M = map(int, sys.stdin.readline().strip().split())
num_list: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

maximum: int = -float('inf')

# case 1 : 일자
# 세로
for i in range(N - 3):
    for j in range(M):
        maximum = max(maximum, num_list[i][j] + num_list[i + 1][j] + num_list[i + 2][j] + num_list[i + 3][j])

# 가로
for i in range(N):
    for j in range(M - 3):
        maximum = max(maximum, num_list[i][j] + num_list[i][j + 1] + num_list[i][j + 2] + num_list[i][j + 3])

# case 2 : 네모
# 네모는 케이스가 단 하나!
for i in range(N - 1):
    for j in range(M - 1):
        maximum = max(maximum, num_list[i][j] + num_list[i + 1][j] + num_list[i][j + 1] + num_list[i + 1][j + 1])

# case 3 : 3 * 2와 2 * 3을 활용하는 나머지 애들
# 3 * 2 (세로, 가로)
for i in range(N - 2):
    for j in range(M - 1):
        maximum = max(maximum, 
                      num_list[i][j] + num_list[i + 1][j] + num_list[i + 2][j] + num_list[i + 2][j + 1],
                      num_list[i][j] + num_list[i][j + 1] + num_list[i + 1][j + 1] + num_list[i + 2][j + 1],
                      num_list[i + 2][j] + num_list[i + 2][j + 1] + num_list[i + 1][j + 1] + num_list[i][j + 1],
                      num_list[i][j] + num_list[i][j + 1] + num_list[i + 1][j] + num_list[i + 2][j],
                      num_list[i][j] + num_list[i + 1][j] + num_list[i + 1][j + 1] + num_list[i + 2][j + 1],
                      num_list[i][j + 1] + num_list[i + 1][j + 1] + num_list[i + 1][j] + num_list[i + 2][j],
                      num_list[i][j] + num_list[i + 1][j] + num_list[i + 2][j] + num_list[i + 1][j + 1],
                      num_list[i][j + 1] + num_list[i + 1][j + 1] + num_list[i + 2][j + 1] + num_list[i + 1][j])

# 2 * 3 (세로, 가로)
for i in range(N - 1):
    for j in range(M - 2):
        maximum = max(maximum, 
                      num_list[i][j] + num_list[i][j + 1] + num_list[i][j + 2] + num_list[i + 1][j],
                      num_list[i + 1][j] + num_list[i + 1][j + 1] + num_list[i + 1][j + 2] + num_list[i][j + 2],
                      num_list[i][j] + num_list[i + 1][j] + num_list[i + 1][j + 1] + num_list[i + 1][j + 2],
                      num_list[i][j] + num_list[i][j + 1] + num_list[i][j + 2] + num_list[i + 1][j + 2],
                      num_list[i][j] + num_list[i][j + 1] + num_list[i + 1][j + 1] + num_list[i + 1][j + 2],
                      num_list[i + 1][j] + num_list[i + 1][j + 1] + num_list[i][j + 1] + num_list[i][j + 2],
                      num_list[i][j] + num_list[i][j + 1] + num_list[i][j + 2] + num_list[i + 1][j + 1],
                      num_list[i + 1][j] + num_list[i + 1][j + 1] + num_list[i + 1][j + 2] + num_list[i][j + 1])

print(f'{maximum}')
