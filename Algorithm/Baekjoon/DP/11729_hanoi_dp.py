import sys

K: int = int(sys.stdin.readline().strip())

def hanoi(N, start, to, via):
    if N == 1:
        print(f'{start} {to}')
    else:
        hanoi(N-1, start, via, to)
        print(f'{start} {to}')
        hanoi(N-1, via, to, start)

print(f'{2 ** K - 1}')
hanoi(K, 1, 3, 2)