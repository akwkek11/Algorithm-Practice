import sys

num_list: list = list(map(int, sys.stdin.readline().strip().split()))
num_list.sort()

result: int = 0

for i in range(0, len(num_list), 2):
    result += num_list[i]

print(f'{result}')