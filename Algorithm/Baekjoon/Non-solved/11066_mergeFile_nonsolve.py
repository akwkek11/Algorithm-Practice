import heapq
import sys

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    K: int = int(sys.stdin.readline().strip())
    number_map: list = list(map(int, sys.stdin.readline().strip().split()))
    sum_map: heapq = []
    result: int = 0

    while number_map:
        heapq.heappush(sum_map, number_map.pop())

    while len(sum_map) > 1:
        next_num: int = heapq.heappop(sum_map) + heapq.heappop(sum_map)
        result += next_num
        heapq.heappush(sum_map, next_num)

    print(f'{result}')