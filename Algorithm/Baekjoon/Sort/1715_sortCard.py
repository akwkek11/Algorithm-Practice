import heapq
import sys

q: list = []
total_cost: int = 0
result: int = 0
N: int = int(sys.stdin.readline().strip())

for _ in range(N):
    heapq.heappush(q, int(sys.stdin.readline().strip()))

while len(q) > 1:
    total_cost = heapq.heappop(q) + heapq.heappop(q)
    result += total_cost
    heapq.heappush(q, total_cost)

print(f'{result}')