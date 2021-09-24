import sys

N: int = int(sys.stdin.readline().strip())
num_list: list = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    num_list.append((start, end))

num_list.sort(key=lambda x : x[0])
num_list.sort(key=lambda x : x[1])

count: int = 0
next_time: int = 0
for start, end in num_list:
    if next_time <= start:
        count += 1
        next_time = end

print(f'{count}')