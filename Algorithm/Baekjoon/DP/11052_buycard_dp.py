import sys

N: int = int(sys.stdin.readline().strip())

num_list: list = list(map(int, sys.stdin.readline().strip().split()))
num_list.insert(0, 0)

max_list: list = [0]
max_list.append(num_list[1])

for i in range(2, N+1):
    max_cost: int = 0
    for j in range(i//2, i):
        max_cost = max(max_cost, max_list[j] + max_list[i-j])
    max_cost = max(max_cost, num_list[i])
    max_list.append(max_cost)

print(f'{max_list[N]}')