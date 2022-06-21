from typing import List
import itertools

def solution(k: int, dungeons: List[List[int]]) -> int:
    answer: int = 0
    dungeons_case: list = list(itertools.permutations(dungeons))

    for case in dungeons_case:
        total: int = k
        count: int = 0
        for require, use in case:
            if require <= total:
                count += 1
                total -= use

        answer = max(answer, count)
    
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))