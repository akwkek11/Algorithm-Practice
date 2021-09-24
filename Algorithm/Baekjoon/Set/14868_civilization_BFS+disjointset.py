from collections import defaultdict, deque

import sys
import time

# Disjoint Set
class DisjointSet:
    def make_set(self, vertice: int) -> list:
        return [i for i in range(vertice)]

    def __init__(self, vertice: int) -> None:
        self.parent: list = self.make_set(vertice + 1)
        self.group_count: int = 0
        self.size: int = vertice
        
    def find(self, vertice: int) -> int:
        if self.parent[vertice] != vertice:
            self.parent[vertice] = self.find(self.parent[vertice])

        return self.parent[vertice]

    def union(self, vertice1: int, vertice2: int) -> None:
        root1: int = self.find(vertice1)
        root2: int = self.find(vertice2)
        if root1 != root2:
            if root1 < root2:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2

    def counting(self) -> None:
        for i in range(1, self.size + 1):
            if self.parent[i] == i:
                self.group_count += 1

N, K = map(int, sys.stdin.readline().strip().split())
civil_map: list = [[0 for _ in range(N)] for _ in range(N)]
disjoint_set: DisjointSet = DisjointSet(K)

# reclamation queue
q: deque = deque(())
q2: deque = deque(())
q3: deque = deque(())

civil_number: int = 0
for _ in range(K):
    civil_number += 1
    x, y = map(int, sys.stdin.readline().strip().split())
    civil_map[x - 1][y - 1] = civil_number
    q.append((x - 1, y - 1))
    q2.append((x - 1, y - 1))
    
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

# 초기 인접 문명 체크.
def init_bfs(x: int, y: int) -> None:
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if civil_map[next_x][next_y] != 0:
                if civil_map[next_x][next_y] != civil_map[x][y]:
                    disjoint_set.union(civil_map[x][y], civil_map[next_x][next_y])

# 간척사업, 큐 2개를 번갈아 사용하면서 연결됐는지 체크해주기.
is_q2_used: bool = True
def bfs(x: int, y: int) -> None:
    is_added: bool = False
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if civil_map[next_x][next_y] == 0:
                civil_map[next_x][next_y] = civil_map[x][y]
                q3.append((next_x, next_y)) if is_q2_used else q2.append((next_x, next_y))
                for i in range(len(dx)):
                    next_x += dx[i]
                    next_y += dy[i]
                    if 0 <= next_x < N and 0 <= next_y < N: 
                        if civil_map[next_x][next_y] != 0 and civil_map[next_x][next_y] != civil_map[x][y]:
                            disjoint_set.union(civil_map[x][y], civil_map[next_x][next_y])
                    next_x -= dx[i]
                    next_y -= dy[i]
            else:
                if civil_map[next_x][next_y] != civil_map[x][y]:
                    disjoint_set.union(civil_map[x][y], civil_map[next_x][next_y])

while q:
    target_x, target_y = q.popleft()
    init_bfs(target_x, target_y)

count: int = 0
while True:
    disjoint_set.counting()
    if disjoint_set.group_count == 1:
        break
    disjoint_set.group_count = 0

    while q2:
        target_x, target_y = q2.popleft()
        bfs(target_x, target_y)
    is_q2_used = False
    count += 1

    disjoint_set.counting()
    if disjoint_set.group_count == 1:
        break
    disjoint_set.group_count = 0

    while q3:
        target_x, target_y = q3.popleft()
        bfs(target_x, target_y)
    is_q2_used = True
    count += 1

print(f'{count}')