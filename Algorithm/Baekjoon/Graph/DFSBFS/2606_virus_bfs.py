import sys
from collections import deque

computer: int = int(sys.stdin.readline().strip())
computer_map: list = [[] for _ in range(computer+1)]
node_num: int = int(sys.stdin.readline().strip())
is_visited: list = [0 for _ in range(computer+1)]
count: int = 0
bfs_queue: deque = deque()

def BFS(target):
    global computer_map
    global is_visited
    global bfs_queue

    for i in computer_map[target]:
        if is_visited[i] == 0:
            is_visited[i] = 1
            bfs_queue.append(i)

for _ in range(node_num):
    a, b = map(int, sys.stdin.readline().strip().split())
    computer_map[a].append(b)
    computer_map[b].append(a)

for i in range(len(computer_map)):
    computer_map[i].sort()

bfs_queue.append(1)
while bfs_queue:
    next_node = bfs_queue.popleft()
    is_visited[next_node] = 1
    count += 1
    BFS(next_node)
count -= 1

print(f'{count}', end='')