import sys

def mul(a: int, b: int, c: int) -> int:
    return (a * b) % c

A, B, C = map(int, sys.stdin.readline().strip().split())

answer: list = []
while B > 0:
    if B % 2 == 1:
        answer.append(mul(1, A, C))
    A = mul(A, A, C)
    B //= 2

res: int = 1
for i in answer:
    res *= i
print(f'{res % C}')