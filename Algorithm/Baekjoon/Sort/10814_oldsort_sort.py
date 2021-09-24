from collections import defaultdict

import sys

N: int = int(sys.stdin.readline().strip())
people_list: defaultdict = defaultdict(list)
age_list: list = []
age_count: list = [0 for _ in range(201)]

for _ in range(N):
    number, name = map(str, sys.stdin.readline().strip().split())
    people_list[int(number)].append(name)
    age_list.append(int(number))

age_list.sort(reverse=True)

while age_list:
    target: int = age_list.pop()
    print(f'{target} {people_list[target][age_count[target]]}')
    age_count[target] += 1