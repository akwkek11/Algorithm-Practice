import sys

N: int = int(sys.stdin.readline().strip())
num_list: list = list(map(int, sys.stdin.readline().strip().split()))
num_list.sort(reverse=True)
sum_list: list = []

while num_list:
    if not sum_list:
        sum_list.append(num_list.pop())
    else:
        sum_list.append(sum_list[-1] + num_list.pop())

print(f'{sum(sum_list)}')