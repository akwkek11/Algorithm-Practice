import sys

def matrix_mul(a: list, b: list) -> list:
    res: list = [[0 for _ in range(len(a))] for _ in range(len(b))]
    
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(a)):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= 1000

    return res

N, B = map(int, sys.stdin.readline().strip().split())
mat: list = [[] for _ in range(N)]
for i in range(N):
    mat[i] = list(map(int, sys.stdin.readline().strip().split()))

answer = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            answer[i][j] = 1

while B > 0:
    if B % 2 == 1:
        answer = matrix_mul(answer, mat)
    
    mat = matrix_mul(mat, mat)
    B //= 2

for in_list in answer:
    for i in range(len(in_list)):
        print(f'{in_list[i]}', end=' ') if i != len(in_list) - 1 else print(f'{in_list[i]}', end='')
    print()