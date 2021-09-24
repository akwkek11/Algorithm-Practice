import sys
n: int = int(sys.stdin.readline().strip())
score_list: list = list(map(int, sys.stdin.readline().strip().split()))
score_list.sort()

min: int = score_list[0]
max: int = score_list[n-1]
print(f'{max-min}')