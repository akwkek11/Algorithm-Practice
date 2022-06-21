import sys

def matrix_mul22(a: list, b: list) -> list:
    res: list = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            res[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
            res[i][j] %= 1000000007

    return res

ans: list = [[1, 0], [0, 1]]
start: list = [[1, 1], [1, 0]]

a = int(sys.stdin.readline().strip())
if a % 2 == 1:
    a += 1
while a > 0:
    if a % 2 == 1:
        ans = matrix_mul22(ans, start)
    start = matrix_mul22(start, start)
    a //= 2

print(f'{ans[0][1]}')