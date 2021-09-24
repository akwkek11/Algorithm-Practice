'''
2021-07-27
'''
import heapq

def solution(jobs: list) -> int:
    '''
        https://programmers.co.kr/learn/courses/30/lessons/42627
    '''
    answer: int = 0
    jobs.sort(key = lambda x: (x[0], x[1]))
    job_heap: heapq = []
    start: int = -1
    now: int = 0
    count: int = 0
    answer: int = 0

    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(job_heap, (job[1], job[0]))
        if len(job_heap) >= 1:
            current_job = heapq.heappop(job_heap)
            count += 1
            start = now
            now += current_job[0]
            answer += now - current_job[1]
        else:
            now += 1
    answer = answer // len(jobs)
    return answer

print(solution([[0, 3], [1, 9], [1, 9], [2, 6]]))
print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]))
print(solution([[0, 3], [0, 2], [1, 9], [2, 6]]))