import sys

num_map = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(101)]
division: int = 10 ** 9

for i in range(1, 10):
    num_map[1][i][1 << i] = 1

for i in range(2, 101):
    for j in range(10):
        for k in range(1024):
            if j == 0:
                num_map[i][j][k | (1 << j)] += num_map[i - 1][j + 1][k]
                num_map[i][j][k | (1 << j)] %= division
            elif j == 9:
                num_map[i][j][k | (1 << j)] += num_map[i - 1][j - 1][k]
                num_map[i][j][k | (1 << j)] %= division
            else:
                num_map[i][j][k | (1 << j)] += (num_map[i - 1][j - 1][k] + num_map[i - 1][j + 1][k])
                num_map[i][j][k | (1 << j)] %= division

target: int = int(sys.stdin.readline().strip())
result: int = 0
for i in range(10):
    result += num_map[target][i][1023]
    result %= division
print(f'{result}')