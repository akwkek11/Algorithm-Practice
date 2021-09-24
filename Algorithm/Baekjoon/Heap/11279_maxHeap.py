import heapq
import sys

N: int = int(sys.stdin.readline().strip())
q: list = []

for _ in range(N):
    result: int = 0
    command: int = int(sys.stdin.readline().strip())
    
    if command == 0:
        if len(q) == 0:
            result = 0
        else:
            result = heapq.heappop(q)[1]
        print(result)
    
    else:
        heapq.heappush(q, (command*(-1), command))