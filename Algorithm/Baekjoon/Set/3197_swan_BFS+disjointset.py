from collections import defaultdict, deque

import sys

# Disjoint Set
class DisjointSet:
    def make_set(self, vertice: int) -> list:
        return [i for i in range(vertice + 1)]

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

R, C = map(int, sys.stdin.readline().strip().split())
str_map: list = [str(sys.stdin.readline().strip()) for _ in range(R)]

converted_map: list = [[0 for _ in range(C)] for _ in range(R)]
swan_list: list = []
for i in range(R):
    for j in range(C):
        if str_map[i][j] == '.':
            converted_map[i][j] = 0
        elif str_map[i][j] == 'X':
            converted_map[i][j] = -1
        elif str_map[i][j] == 'L':
            converted_map[i][j] = 0
            swan_list.append((i, j))

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

# init queue
q: deque = deque(())

# reclamation queue
q2: deque = deque(())
q3: deque = deque(())

def bfs(x: int, y: int) -> None:
    is_added: bool = False
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < R and 0 <= next_y < C:
            if converted_map[next_x][next_y] == 0:
                converted_map[next_x][next_y] = converted_map[x][y]
                q.append((next_x, next_y))
            elif converted_map[next_x][next_y] == -1:
                if not is_added:
                    q2.append((x, y))
                    is_added = True

# 1. 섬에 라벨링
island_num: int = 0
for i in range(R):
    for j in range(C):
        if converted_map[i][j] == 0:
            island_num += 1
            converted_map[i][j] = island_num
            q.append((i, j))
            while q:
                target_x, target_y = q.popleft()
                bfs(target_x, target_y)

disjoint_set: DisjointSet = DisjointSet(island_num)

'''
for i in range(R):
    for j in range(C):
        print(f'{converted_map[i][j]}', end = ' ') if j != C - 1 else print(f'{converted_map[i][j]}')
'''

# 2. 간척사업, 큐 2개를 번갈아 사용하면서 연결됐는지 체크해주기.
is_q2_used: bool = True
def bfs2(x: int, y: int) -> None:
    is_added: bool = False
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < R and 0 <= next_y < C:
            if converted_map[next_x][next_y] == -1:
                converted_map[next_x][next_y] = converted_map[x][y]
                q3.append((next_x, next_y)) if is_q2_used else q2.append((next_x, next_y))
                for i in range(len(dx)):
                    next_x += dx[i]
                    next_y += dy[i]
                    if 0 <= next_x < R and 0 <= next_y < C: 
                        if converted_map[next_x][next_y] != -1 and converted_map[next_x][next_y] != converted_map[x][y]:
                            disjoint_set.union(converted_map[x][y], converted_map[next_x][next_y])
                    next_x -= dx[i]
                    next_y -= dy[i]
            else:
                if converted_map[next_x][next_y] != converted_map[x][y]:
                    disjoint_set.union(converted_map[x][y], converted_map[next_x][next_y])

count: int = 0
while True:
    if disjoint_set.find(converted_map[swan_list[0][0]][swan_list[0][1]]) == disjoint_set.find(converted_map[swan_list[1][0]][swan_list[1][1]]):
        break

    while q2:
        target_x, target_y = q2.popleft()
        bfs2(target_x, target_y)
    is_q2_used = False
    count += 1

    if disjoint_set.find(converted_map[swan_list[0][0]][swan_list[0][1]]) == disjoint_set.find(converted_map[swan_list[1][0]][swan_list[1][1]]):
        break

    while q3:
        target_x, target_y = q3.popleft()
        bfs2(target_x, target_y)
    is_q2_used = True
    count += 1

print(f'{count}')