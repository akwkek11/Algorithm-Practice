import sys

def matrix_mul22(a: list, b: list) -> list:
    res: list = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            res[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
            res[i][j] %= 1000000007

    return res

ans: list = [[1, 0], [0, 1]]
a: list = [[1, 1], [1, 0]]

N: int = int(sys.stdin.readline().strip())

while N > 0:
    if N % 2 == 1:
        ans = matrix_mul22(ans, a)
    a = matrix_mul22(a, a)

    N //= 2

print(f'{ans[0][1]}')