from collections import defaultdict
import sys

N, M = map(int, sys.stdin.readline().strip().split())

word_dict: defaultdict = defaultdict(int)
for _ in range(N):
    word_dict[str(sys.stdin.readline().strip())] = 1

count: int = 0
for _ in range(M):
    if word_dict[str(sys.stdin.readline().strip())] == 1:
        count += 1

print(f'{count}')