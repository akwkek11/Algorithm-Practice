import sys

N, M = map(int, sys.stdin.readline().strip().split())

memory: list = list(map(int, sys.stdin.readline().strip().split()))
cost: list = list(map(int, sys.stdin.readline().strip().split()))
total: list = [[0 for _ in range(sum(cost) + 1)] for _ in range(N)]

result: int = float('inf')
for i in range(N):
	now_mem: int = memory[i]
	now_cost: int = cost[i]
	for j in range(sum(cost) + 1):
		if i == 0:
			if j >= now_cost:
				total[i][j] = now_mem
		else:
			if j >= now_cost:
				total[i][j] = max(total[i - 1][j - now_cost] + now_mem, total[i - 1][j])
			else:
				total[i][j] = total[i - 1][j]

		if total[i][j] >= M:
			result = min(result, j)

print(f'{result}')