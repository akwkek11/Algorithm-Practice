from collections import deque

import sys

N: int = int(sys.stdin.readline().strip())
word_list: list = []

for _ in range(N):
    in_str: str = str(sys.stdin.readline().strip())
    word_list.append(in_str)

word_list.sort()
word_queue: deque = deque(word_list)
word_save: list = []

is_prefix: bool = False
while word_queue:
    is_prefix = False
    target: str = word_queue.popleft()
    for word in list(word_queue):
        if word.startswith(target):
            is_prefix = True
            break
    
    if not is_prefix:
        word_save.append(target)

print(f'{len(word_save)}')