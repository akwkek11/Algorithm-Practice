from collections import deque

def solution(priorities: list, location: int):
    # q1은 프린터 큐, q2는 이를 따라가는 인덱스 큐
    q1: deque = deque(priorities)
    q2: deque = deque([i for i in range(len(priorities))])

    # q2 인덱스 순서 저장
    result: list = []

    while q1:
        value: int = q1.popleft()
        index: int = q2.popleft()
        is_changed: bool = False

        for i in list(q1):
            if value < i:
                is_changed = True
                break
        
        if is_changed:
            q1.append(value)
            q2.append(index)
        else:
            result.append(index)

    answer: int = result.index(location) + 1
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))