import sys

N, T = map(int, sys.stdin.readline().strip().split())
score_list: list = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
sum_list: list = [0 for _ in range(T + 1)]

for i in range(N):
    for j in range(T, 1, -1):
        if score_list[i][0] <= j:
            sum_list[j] = max(sum_list[j - score_list[i][0]] + score_list[i][1], sum_list[j])

print(sum_list[T])