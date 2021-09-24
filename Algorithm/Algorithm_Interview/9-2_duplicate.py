from collections import Counter

import sys

s: str = str(sys.stdin.readline().strip())
counter, stack = Counter(s), []

for i in s:
    counter[i] -= 1
    if i in stack:
        continue

    while stack and i < stack[-1] and counter[stack[-1]] > 0:
        stack.pop()
    stack.append(i)

print(''.join(stack))