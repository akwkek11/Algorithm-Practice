from collections import deque

import re
import sys

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    cmd: str = str(sys.stdin.readline().strip())
    list_size: int = int(sys.stdin.readline().strip())
    target_list: list = list(map(str, re.sub(r'[^a-zA-Z0-9]', ' ', str(sys.stdin.readline().strip())).strip().split()))

    q: deque = deque(target_list)
    reverse_check: bool = False
    empty_pop: bool = False
    for i in range(len(cmd)):
        if cmd[i] == 'R':
            reverse_check = True if not reverse_check else False
        elif cmd[i] == 'D':
            if not q:
                print('error')
                empty_pop = True
                break
            q.popleft() if not reverse_check else q.pop()

    if not empty_pop:
        if reverse_check:
            q.reverse()

        print('[', end='')
        while q:
            target: str = q.popleft()
            print(f'{target}', end=',') if q else print(f'{target}', end='')
        print(']')