import heapq
import sys

N: int = int(sys.stdin.readline().strip())
max_heap: list = []
min_heap: list = []

for _ in range(N):
    number: int = int(sys.stdin.readline().strip())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-number, number))
    else:
        heapq.heappush(min_heap, (number, number))
    
    if len(max_heap) >= 1 and len(min_heap) >=1 and max_heap[0][1] > min_heap[0][1]:
        max_num: int = heapq.heappop(max_heap)[1]
        min_num: int = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-min_num, min_num))
        heapq.heappush(min_heap, (max_num, max_num))
    
    print(f'{max_heap[0][1]}')