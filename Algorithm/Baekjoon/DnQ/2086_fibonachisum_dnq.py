import sys

def matrix_mul22(a: list, b: list) -> list:
    res: list = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            res[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
            res[i][j] %= 1000000000

    return res

ans1: list = [[1, 0], [0, 1]]
ans2: list = [[1, 0], [0, 1]]
start: list = [[1, 1], [1, 0]]
end: list = [[1, 1], [1, 0]]

a, b = map(int, sys.stdin.readline().strip().split())
a += 1
b += 2
while a > 0:
    if a % 2 == 1:
        ans1 = matrix_mul22(ans1, start)
    start = matrix_mul22(start, start)

    a //= 2

while b > 0:
    if b % 2 == 1:
        ans2 = matrix_mul22(ans2, end)
    end = matrix_mul22(end, end)

    b //= 2

result: int = ans2[0][1] - ans1[0][1]
if result < 0:
    result += 1000000000
print(f'{result}')