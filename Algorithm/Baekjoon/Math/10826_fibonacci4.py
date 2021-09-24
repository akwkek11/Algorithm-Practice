import sys

num_list: list = [0, 1, 1]
N: int = int(sys.stdin.readline().strip())

for _ in range(len(num_list) - 1, N):
    num_list.append(num_list[-2] + num_list[-1])

print(f'{num_list[-1]}') if N != 0 else print('0')