from collections import Counter

import sys

J: str = str(sys.stdin.readline().strip())
S: str = str(sys.stdin.readline().strip())

count: Counter = Counter(S)
result: int = 0
for i in J:
    result += count[i]
print(f'{result}')