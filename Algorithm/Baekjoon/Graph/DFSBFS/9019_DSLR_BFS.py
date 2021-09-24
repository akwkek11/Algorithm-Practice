from collections import deque

import sys

def bfs(now: int, cmd: int) -> None:
    # D
    next_now: int = (now * 2) % 10000
    if is_visited[next_now] == 0:
        is_visited[next_now] = 1
        q.append((next_now, cmd + 'D'))
    
    # S
    next_now = now - 1 if now != 0 else 9999
    if is_visited[next_now] == 0:
        is_visited[next_now] = 1
        q.append((next_now, cmd + 'S'))

    # L
    next_now = (now * 10 + (now // 1000)) % 10000
    if is_visited[next_now] == 0:
        is_visited[next_now] = 1
        q.append((next_now, cmd + 'L'))

    # R
    next_now = (now // 10) + (now % 10) * 1000
    if is_visited[next_now] == 0:
        is_visited[next_now] = 1
        q.append((next_now, cmd + 'R'))

    return

T: int = int(sys.stdin.readline().strip())
for i in range(T):
    q: deque = deque(())
    is_visited = [0 for _ in range(10000)]
    start, end = map(int, sys.stdin.readline().strip().split())
    q.append((start, ''))
    while q:
        target_num, now_command = q.popleft()
        if target_num == end:
            print(now_command)

        else:
            bfs(target_num, now_command)