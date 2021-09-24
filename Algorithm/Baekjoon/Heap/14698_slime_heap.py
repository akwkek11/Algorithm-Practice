import heapq
import sys

T: int = int(sys.stdin.readline().strip())
min_heap: heapq = None
result: int = 1
remainder: int = 1000000007

for _ in range(T):
    N: int = int(sys.stdin.readline().strip())
    min_heap = list(map(int, sys.stdin.readline().strip().split()))
    heapq.heapify(min_heap)
    
    while len(min_heap) > 1:
        num1: int = heapq.heappop(min_heap)
        num2: int = heapq.heappop(min_heap)

        result *= ((num1 % remainder) * (num2 % remainder)) % remainder
        result %= remainder
        heapq.heappush(min_heap, num1 * num2)

    print(f'{result}')
    result = 1