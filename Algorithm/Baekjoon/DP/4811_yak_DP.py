from collections import deque

import math
import sys

def catalan(n: int) -> int:
    return math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))

input_list = []

while True:
    int_in: int = int(sys.stdin.readline().strip())
    if int_in == 0:
        q: deque = deque(input_list)
        while q:
            print(f'{catalan(q.popleft())}')
        break
    else:
        input_list.append(int_in)