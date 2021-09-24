import sys

from collections import deque

n: int = int(sys.stdin.readline().strip())
printer_queue: deque = deque()

for _ in range(n):
    count: int = 0
    maximum: int = 0
    maximum_index: int = 0

    length, target = map(int, sys.stdin.readline().strip().split())
    temp_list: list = list(map(int, sys.stdin.readline().strip().split()))
    
    for i in range(len(temp_list)):
        printer_queue.append((i, temp_list[i]))

    while True:
        maximum: int = 0
        maximum_index: int = 0
        index_count: int = 0

        for i in list(printer_queue):
            if maximum < i[1]:
                maximum = i[1]
                maximum_index = index_count
            index_count += 1

        for _ in range(0, maximum_index):
            printer_queue.rotate(-1)
            
        index, weight = printer_queue.popleft()
        count += 1
        if index == target:
            break

    print(count)
    printer_queue.clear()
    
