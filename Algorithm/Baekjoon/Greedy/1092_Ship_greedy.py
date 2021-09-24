'''
    항상 최소부터 뽑는다해서 최소로 가는게 최적이 아니라,
    반대로 계산하는 것이 최적일 때도 존재한다는 것을 기억하자.
'''

from collections import deque

import sys

N: int = int(sys.stdin.readline().strip())
crane_list: list = list(map(int, sys.stdin.readline().strip().split()))
M : int = int(sys.stdin.readline().strip())
weight_list: list = list(map(int, sys.stdin.readline().strip().split()))
crane_list.sort(reverse = True)
weight_list.sort()
stack: list = []

is_too_heavy: bool = False
is_disabled: bool = False

count: int = 0
while weight_list:
    i: int = 0
    next_target: int = float('inf')
    while i < N:
        if weight_list:
            next_target = weight_list.pop()
            if crane_list[0] < next_target:
                is_too_heavy = True
                break 
        
        if not weight_list:
            if crane_list[i] < next_target:
                weight_list.append(next_target)
            while stack:
                weight_list.append(stack.pop())
            
            break
        else:
            if crane_list[i] < weight_list[0]:
                weight_list.append(next_target)
                while stack:
                    weight_list.append(stack.pop())
                break

            elif crane_list[i] < next_target:
                stack.append(next_target)
            elif crane_list[i] >= next_target:
                i += 1
                if i == N:
                    while stack:
                        weight_list.append(stack.pop())
                    break

    if is_too_heavy:
        break
    
    count += 1

print('-1') if is_too_heavy else print(f'{count}')