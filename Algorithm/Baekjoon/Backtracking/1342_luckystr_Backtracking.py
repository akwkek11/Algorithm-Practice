from collections import Counter

import math
import sys

s: str = str(sys.stdin.readline().strip())
count: dict = dict(Counter(s))
result: int = 0

def DFS(now_str: str) -> None:
    global s
    global count
    global result

    str_list: list = [now_str]
    
    if len(now_str) == len(s):
        result += 1
        return
    
    is_unique: bool = True
    for key, value in count.items():
        if len(now_str) == 0:
            if value >= 2:
                is_unique = False
                break

        elif (now_str[-1] == key and value >= 1) or (now_str[-1] != key and value >= 2):
            is_unique = False
            break

    if is_unique:
        key_count: int = 0
        for key, value in count.items():
            if value == 1:
                key_count += 1
        
        result += math.factorial(key_count)
        return

    for key, value in count.items():
        if value > 0 and (len(now_str) == 0 or now_str[-1] != key):     
            str_list.append(key)
            count[key] -= 1
            DFS(''.join(str_list))
            count[key] += 1
            str_list.pop()

DFS('')
print(f'{result}')