import sys

T: int = int(sys.stdin.readline().strip())
num_map: list = [[0 for _ in range(1001)] for _ in range(1001)]
mod: int = 10 ** 9 + 9
num_map[1][1] = 1
num_map[2][1] = 1
num_map[2][2] = 1
num_map[3][1] = 1
num_map[3][2] = 2
num_map[3][3] = 1

for i in range(4, 1001):
    for j in range(1, i + 1):
        for k in range(1, 4):
            num_map[i][j] += num_map[i - k][j - 1]
        num_map[i][j] %= mod

for _ in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(f'{num_map[n][m] % mod}')