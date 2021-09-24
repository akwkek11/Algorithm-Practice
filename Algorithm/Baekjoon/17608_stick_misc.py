import sys

n: int = int(sys.stdin.readline().strip())
stick_list: list = [0 for _ in range(n)]
max_len: int = 0
result: int = 0

for i in range(n):
    stick_list[i] = int(sys.stdin.readline().strip())

for i in range(len(stick_list)-1, -1, -1):
    if max_len < stick_list[i]:
        max_len = stick_list[i]
        result += 1

print(f'{result}')