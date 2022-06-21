from typing import List
import heapq

def solution(n: int, works: List[int]) -> int:
    if n >= sum(works):
        return 0
    
    work_heap: heapq = []
    while works:
        work_overload: int = works.pop()
        heapq.heappush(work_heap, (-work_overload, work_overload))
    
    while n >= 1:
        now_max: int = heapq.heappop(work_heap)[1]
        now_max -= 1
        heapq.heappush(work_heap, (-now_max, now_max))
        n -= 1

    answer: int = 0
    for index, value in work_heap:
        answer += value ** 2
    return answer

print(solution([4, 3, 3], 4))