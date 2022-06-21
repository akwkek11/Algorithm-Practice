from typing import List
from collections import defaultdict
from bisect import bisect_left

import itertools

def solution(info: List[str], query: List[str]) -> List[int]:
    answer: List[int] = []
    database: defaultdict = defaultdict(list)
    for data in info:
        data_list: List[str] = data.split(' ')
        data_int: int = int(data_list.pop())
        for i in range(1, 5):
            keys: List[tuple] = list(itertools.combinations(data_list, i))
            for key in keys:
                database[key].append(data_int)
        database[(0,)].append(data_int)

    for key in database:
        database[key].sort()
    
    for q in query:
        result_query: List[str] = []
        query_split: List[str] = q.split(' ')
        for word in query_split:
            if word not in ['-', 'and']:
                result_query.append(word)

        if len(result_query) == 1:
            temp_int: int = result_query.pop()
            result_query.append(0)
            result_query.append(temp_int)

        result_data: List[int] = database[tuple(result_query[:len(result_query) - 1])]
        compare_score: int = int(result_query[-1])
        answer.append(len(result_data) - bisect_left(result_data, compare_score))
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))