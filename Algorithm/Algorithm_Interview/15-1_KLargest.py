import heapq

def solution(num_list: list, k: int) -> int:
    result: int = 0

    num_heap: heapq = [(-1) * i for i in num_list]
    heapq.heapify(num_heap)
    for _ in range(k):
        result = heapq.heappop(num_heap)
    return (-1) * result

print(f'{solution([3, 2, 3, 1, 2, 4, 5, 4, 6], 4)}')