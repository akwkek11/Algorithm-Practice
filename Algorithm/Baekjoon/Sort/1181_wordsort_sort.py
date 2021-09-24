from collections import defaultdict

import sys

N: int = int(sys.stdin.readline().strip())
word_dict: defaultdict = defaultdict(int)

for _ in range(N):
    input_str: str = str(sys.stdin.readline().strip())
    if word_dict[input_str] == 0:
        word_dict[input_str] = 1

res_list: list = [key for key in word_dict.keys()]
res_list.sort()
res_list = sorted(res_list, key=len)

for word in res_list:
    print(f'{word}')