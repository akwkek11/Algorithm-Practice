from collections import defaultdict

import sys

N, M = map(int, sys.stdin.readline().strip().split())
know_list: list = list(map(int, sys.stdin.readline().strip().split()))
del know_list[0]

know_dict: defaultdict = defaultdict(int)
for i in know_list:
    know_dict[i] = 1

party_list: list = []
for _ in range(M):
    number, *people = map(int, sys.stdin.readline().strip().split())
    party_list.append(people)

for _ in range(M // 2 + 1):
    for i in range(len(party_list)):
        for j in party_list[i]:
            if know_dict[j] == 1:
                for k in party_list[i]:
                    know_dict[k] = 1
                break

    for i in range(len(party_list) - 1, -1, -1):
        for j in party_list[i]:
            if know_dict[j] == 1:
                for k in party_list[i]:
                    know_dict[k] = 1
                break

count: int = 0
for i in range(len(party_list)):
    is_known = False
    for j in party_list[i]:
        if know_dict[j] == 1:
            is_known = True
            break

    count += 1 if not is_known else 0

print(f'{count}')