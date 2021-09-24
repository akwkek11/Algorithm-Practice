import heapq

def solution(n: int, lost: list, reserve: list) -> int:
    answer: int = 0
    lost_reserve: list = []
    always_lost: list = []
    for i in reserve:
        if i in lost:
            lost_reserve.append(i)

    for i in lost_reserve:
        lost.remove(i)
        reserve.remove(i)

    heapq.heapify(lost)
    heapq.heapify(reserve)

    while lost:
        is_match: bool = False
        a: int = heapq.heappop(lost)

        while reserve:
            b: int = heapq.heappop(reserve)

            if b - 1 == a or b + 1 == a:
                is_match = True
                break

            else:
                if b < a:
                    continue

                else:
                    heapq.heappush(reserve, b)
                    break
        
        if not is_match:
            always_lost.append(a)

    answer = n - len(always_lost)
    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))