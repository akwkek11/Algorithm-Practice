import heapq
import sys

n, m = map(int, sys.stdin.readline().strip().split())
priority_queue: heapq = []
num_list: list = list(map(int, sys.stdin.readline().strip().split()))

for i in num_list:
    heapq.heappush(priority_queue, i)

for i in range(m):
    num1: int = heapq.heappop(priority_queue)
    num2: int = heapq.heappop(priority_queue)

    for j in range(2):
        heapq.heappush(priority_queue, num1 + num2)

print(f'{sum(priority_queue)}')