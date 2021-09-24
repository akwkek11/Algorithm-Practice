import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().strip().split())

node_map: list = [[] for _ in range(N+1)]
is_visited: list = [0 for _ in range(N+1)]
dfs_search: list = []
bfs_search: list = []
bfs_queue: deque = deque()

def DFS(start: int) -> None:
    global node_map
    global is_visited
    global dfs_search

    for i in node_map[start]:
        if is_visited[i] == 0:
            is_visited[i] = 1
            dfs_search.append(i)
            DFS(i)

def BFS(start: int) -> None:
    global node_map
    global is_visited
    global bfs_search

    for i in node_map[start]:
        if is_visited[i] == 0:
            is_visited[i] = 1
            bfs_queue.append(i)

def print_list(target_list: list) -> None:
    for i in range(len(target_list)):
        print(f'{target_list[i]}', end='')
        if i != len(target_list) - 1:
            print('', end=' ')
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    node_map[a].append(b)
    node_map[b].append(a)

for i in range(len(node_map)):
    node_map[i].sort()

# DFS
is_visited[V] = 1
dfs_search.append(V)
DFS(V)

for i in range(len(is_visited)):
    is_visited[i] = 0

# BFS
bfs_queue.append(V)
while bfs_queue:
    next_node: int = bfs_queue.popleft()
    is_visited[next_node] = 1
    bfs_search.append(next_node)
    BFS(next_node)

print_list(dfs_search)
print()
print_list(bfs_search)