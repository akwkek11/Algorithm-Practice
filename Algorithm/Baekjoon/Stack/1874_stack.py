from typing import List

import sys

N: int = int(sys.stdin.readline().strip())
n_map: List[int] = [i for i in range(1, N+1)]
target_map: List[int] = []
stack: List[int] = []
command: List[str] = []

count: int = 1
is_vaild: bool = True

for _ in range(N):
    target_map.append(int(sys.stdin.readline().strip()))

for i in range(len(target_map)):
    if i == 0:
        for _ in range(target_map[i]):
            command.append('+')
            stack.append(count)
            count += 1
    
    else:
        if len(stack) == 0:
            for i in range(count, target_map[i]+1):
                command.append('+')
                stack.append(i)
                count += 1
        else:
            now_stack: int = stack.pop()
            if target_map[i] == now_stack:
                stack.append(now_stack)
            else:
                if target_map[i] < now_stack:
                    is_vaild = False
                    break
                else:
                    stack.append(now_stack)
                    for i in range(count, target_map[i]+1):
                        command.append('+')
                        stack.append(i)
                        count += 1
    
    command.append('-')
    target_map.append(stack.pop())

if is_vaild:
    for i in range(len(command)):
        print(f'{command[i]}')
else:
    print('NO')