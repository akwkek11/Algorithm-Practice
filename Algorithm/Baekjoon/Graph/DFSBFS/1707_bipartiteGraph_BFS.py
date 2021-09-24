from collections import deque

import sys

K: int = int(sys.stdin.readline().strip())

def bfs() -> bool:
    bfs_queue: deque = deque()
    for i in range(len(node_map)):
        if len(node_map[i]) > 0 and is_visited[i] == 0:
            is_visited[i] = 1
            bfs_queue.append(i)
            while bfs_queue:
                target: int = bfs_queue.popleft()
                for k in node_map[target]:
                    if is_visited[k] == 0:
                        bfs_queue.append(k)
                        is_visited[k] = is_visited[target] + 1
                    else:
                        if is_visited[k] % 2 == is_visited[target] % 2:
                            return False
    return True

for _ in range(K):
    V, E = map(int, sys.stdin.readline().strip().split())
    node_map: list = [[] for _ in range(V+1)]
    is_visited: list = [0 for _ in range(V+1)]
    for _ in range(E):
        edge1, edge2 = map(int, sys.stdin.readline().strip().split())
        node_map[edge1].append(edge2)
        node_map[edge2].append(edge1)
    
    if V == 1 and E == 1:
        print('YES')
    else:
        print('YES') if bfs() else print('NO')