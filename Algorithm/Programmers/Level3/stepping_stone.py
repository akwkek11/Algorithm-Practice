from collections import deque
 
def solution(stones: list, k: int) -> int:
    result: list = []
    Qi = deque()
    for i in range(k):
        while Qi and stones[i] >= stones[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    for i in range(k, len(stones)):
        result.append(stones[Qi[0]])
        while Qi and Qi[0] <= i-k:
            Qi.popleft()
        while Qi and stones[i] >= stones[Qi[-1]] :
            Qi.pop()
        Qi.append(i)
    result.append(stones[Qi[0]])
    return min(result)

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))