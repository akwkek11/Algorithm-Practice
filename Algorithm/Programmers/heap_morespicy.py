'''
2021-07-27
'''
import heapq

def solution(scoville, K):
    '''
        https://programmers.co.kr/learn/courses/30/lessons/42626
    '''
    answer: int = 0

    heapq.heapify(scoville)
    while len(scoville) > 1:
        min_spicy: int = heapq.heappop(scoville)
        next_spicy: int = heapq.heappop(scoville)
        if min_spicy >= K:
            heapq.heappush(scoville, min_spicy)
            heapq.heappush(scoville, next_spicy)
            break
        heapq.heappush(scoville, min_spicy + next_spicy * 2)
        answer += 1

    if len(scoville) == 1:
        if scoville[0] < K:
            answer = -1
    return answer