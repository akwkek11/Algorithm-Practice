import heapq
import sys

N: int = int(sys.stdin.readline().strip())
q: list = []

for _ in range(N):
    result: int = 0
    command = int(sys.stdin.readline().strip())
    if command == 0:
        if len(q) == 0:
            result = 0
        else:
            result = heapq.heappop(q)
        print(f'{result}')
    else:
        heapq.heappush(q, command)