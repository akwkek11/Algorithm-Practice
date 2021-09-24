from collections import defaultdict, deque

import sys

N: int = int(sys.stdin.readline().strip())
people_list: list = [-1 for _ in range(N + 1)]

connect_dict: defaultdict = defaultdict(list)
for i in range(1, N + 1):
    connection: list = list(map(int, sys.stdin.readline().strip().split()))
    connection.pop()
    connect_dict[i] = connection

start_N: int = int(sys.stdin.readline().strip())
start_people: list = list(map(int, sys.stdin.readline().strip().split()))
q: deque = deque(())

# 1. 초기값 세팅
for start in start_people:
    people_list[start] = 0
    for target in connect_dict[start]:
        q.append((target, 0))

def bfs(who: int, time: int) -> None:
    if people_list[who] != -1:
        return

    connected: int = len(connect_dict[who])
    trust: int = 0
    for i in connect_dict[who]:
        if people_list[i] != -1 and people_list[i] <= time:
            trust += 1
    
    if trust / connected >= 0.5:
        people_list[who] = time + 1

        for target in connect_dict[who]:
            if people_list[target] == -1:
                q.append((target, time + 1))
while q:
    next_target, now_time = q.popleft()
    bfs(next_target, now_time)

del people_list[0]
string_ints: list = [str(i) for i in people_list]
print(' '.join(string_ints))
