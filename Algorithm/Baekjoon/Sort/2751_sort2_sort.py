import heapq
import sys

N: int = int(sys.stdin.readline().strip())
num_list: heapq = [] 
for _ in range(N):
    heapq.heappush(num_list, int(sys.stdin.readline().strip()))

while num_list:
    print(f'{heapq.heappop(num_list)}')