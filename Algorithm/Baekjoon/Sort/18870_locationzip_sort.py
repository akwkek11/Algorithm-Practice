from collections import Counter, defaultdict

import sys

N: int = int(sys.stdin.readline().strip())
num_list: list = list(map(int, sys.stdin.readline().strip().split()))
count_list: list = [key for key in Counter(num_list)]
count_list.sort(reverse=True)
zip_list: defaultdict = defaultdict(int)

index: int = 0
while count_list:
    zip_list[count_list.pop()] = index
    index += 1

for i in num_list:
    print(f'{zip_list[i]}', end=' ')