from collections import defaultdict

import sys

N: int = int(sys.stdin.readline().strip())
alpha_list: list = []
alpha_score: list = [0 for _ in range(10)]
alpha_map: list = [['A', 0], ['B', 1], ['C', 2], ['D', 3], ['E', 4],
                   ['F', 5], ['G', 6], ['H', 7], ['I', 8], ['J', 9]]

for _ in range(N):
    alpha_list.append(str(sys.stdin.readline().strip()))

num_dict: defaultdict = defaultdict(int)
for eng, index in alpha_map:
    num_dict[eng] = index

TF_Table: list = [False for _ in range(10)]
for target_eng in alpha_list:
    for i in range(len(target_eng)):
        if i == 0:
            TF_Table[num_dict[target_eng[i]]] = True
        alpha_score[num_dict[target_eng[i]]] += 10 ** (len(target_eng) - 1 - i)

is_zero: bool = False
for i in alpha_score:
    if i == 0:
        is_zero: bool = True
        break

rank: list = []
while alpha_score:
    eng_score: int = alpha_score.pop()
    if eng_score != 0:
        rank.append((len(alpha_score), eng_score))

true_table: list = []
false_table: list = []
while rank:
    index, eng_score = rank.pop()
    if TF_Table[index] == True:
        true_table.append((index, eng_score))
    else:
        false_table.append((index, eng_score))
    
false_table.sort(key=lambda x: x[1], reverse = True)
if not is_zero and false_table:
    index, final_score = false_table.pop()
    alpha_map[index][1] = 0

while false_table:
    true_table.append(false_table.pop())

true_table.sort(key=lambda x: x[1])
final_number: int = 9
while true_table:
    index, final_score = true_table.pop()
    alpha_map[index][1] = final_number
    final_number -= 1

final_list: list = []
for target_eng in alpha_list:
    convert_eng_to_num: list = []
    for i in range(len(target_eng)):
        convert_eng_to_num.append(str(alpha_map[num_dict[target_eng[i]]][1]))
    final_list.append(int(''.join(convert_eng_to_num)))

print(f'{sum(final_list)}')