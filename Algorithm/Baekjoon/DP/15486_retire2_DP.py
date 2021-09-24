import sys

N: int = int(sys.stdin.readline().strip())
schedule: list = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
schedule.insert(0, (0, 0))
total_sum: list = [0 for _ in range(N + 2)]

answer: int = 0
for i in range(1, N + 1):
    answer = max(answer, total_sum[i])
    if i + schedule[i][0] > N + 1:
        continue
    
    total_sum[i + schedule[i][0]] = max(total_sum[i + schedule[i][0]], answer + schedule[i][1])

answer = max(answer, total_sum[N + 1])
print(f'{answer}')