from collections import defaultdict

import sys

s: str = str(sys.stdin.readline().strip())
index_list: list = []

index: int = 0
while index < len(s):
    alpha_list: defaultdict = defaultdict(int)
    start_index: int = index
    end_index: int = 0
    if alpha_list[s[index]] == 0:
        alpha_list[s[index]] = 1
        for i in range(index + 1, len(s) + 1):
            if i == len(s) or alpha_list[s[i]] == 1:
                end_index = i - 1
                index_list.append((start_index, end_index))
                break
            else:
                alpha_list[s[i]] = 1

    index += 1

index_list.sort(key=lambda x: x[1]-x[0])
s_index, e_index = index_list.pop()
print(f'{e_index - s_index + 1}')