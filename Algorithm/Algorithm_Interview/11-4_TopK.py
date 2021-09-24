from collections import Counter

import sys

number: list = list(map(int, sys.stdin.readline().strip().split()))
count: Counter = Counter(number)

k: int = int(sys.stdin.readline().strip())
final_list: list = [str(key) for key, value in count.most_common(k)]
final_list.sort()
print(' '.join(final_list))