import sys
from collections import deque

N: int = int(sys.stdin.readline().strip())
remainder: int = N % 6
result: list = None
odd_list: list = [i for i in range(1, N + 1, 2)]
even_list: list = [i for i in range(2, N + 1, 2)]

if remainder not in [2, 3]:
    result = odd_list + even_list

else:
    odd_queue: deque = deque(odd_list)
    even_queue: deque = deque(even_list)
    temp_list: list = []

    if remainder == 2:
        for _ in range(3):
            temp_list.append(odd_queue.popleft())
        odd_queue.append(temp_list.pop())
        odd_queue.appendleft(temp_list[0])
        odd_queue.appendleft(temp_list[1])

    elif remainder == 3:
        for _ in range(2):
            temp_list.append(odd_queue.popleft())
        temp_list.append(even_queue.popleft())
        odd_queue.append(temp_list[0])
        odd_queue.append(temp_list[1])
        even_queue.append(temp_list.pop())
    
    result = list(even_queue) + list(odd_queue)

for i in result:
    print(i)