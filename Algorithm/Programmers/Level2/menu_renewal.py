from typing import List
from collections import defaultdict
import itertools

def solution(orders: List[str], course: List[int]) -> List[str]:
    max_len: int = -float('inf')
    for i in orders:
        if max_len <= len(i):
            max_len = len(i)

    set_dict: defaultdict = defaultdict(int)
    for menu in orders:
        for i in range(2, len(menu) + 1):
            for keys in list(itertools.combinations(menu, i)):
                sort_keys: List[str] = list(keys)
                sort_keys.sort()
                set_dict[''.join(sort_keys)] += 1
    
    set_dict_list: List[(str, int)] = list(set_dict.items())
    set_len_list: List[List(str, int)] = [[i for i in set_dict_list if len(i[0]) == j] for j in range(2, max_len + 1)]

    for i in range(max_len - 1):
        set_len_list[i].sort(key=lambda x : x[1], reverse=True)
    
    answer: List[str] = []
    max_count: int = 0
    appended: int = 0
    for length in course:
        if length <= max_len:
            while True:
                if len(set_len_list[length - 2]) == 0 or len(set_len_list[length - 2]) == appended:
                    break

                if max_count == 0:
                    max_count = set_len_list[length - 2][appended][1]
                
                if max_count != set_len_list[length - 2][appended][1] or max_count == 1:
                    break

                answer.append(''.join(set_len_list[length - 2][appended][0]))
                appended += 1
        appended = 0
        max_count = 0

    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))