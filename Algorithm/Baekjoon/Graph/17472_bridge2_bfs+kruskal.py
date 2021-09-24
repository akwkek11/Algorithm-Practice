from collections import deque

import sys

N, M = map(int, sys.stdin.readline().strip().split())
'''
    direction
    0 : all
    1 : up
    2 : down
    3 : left
    4 : right
'''
island: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
is_visited: list = [[0 for _ in range(M)] for _ in range(N)]
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]
q: deque = deque(())

def bfs(start: int, x: int, y: int, direction: int, count: int, is_met: bool) -> None:
    global island_number
    if direction == 0:
        for i in range(len(dx)):
            next_x: int = x + dx[i]
            next_y: int = y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M and is_visited[next_x][next_y] == 0 and island[next_x][next_y] > 0:
                island[next_x][next_y] = island_number
                is_visited[next_x][next_y] = 1
                q.append((start, next_x, next_y, 0, 0, False))
    else:
        next_x: int = x + dx[direction - 1]
        next_y: int = y + dy[direction - 1]
        if 0 <= next_x < N and 0 <= next_y < M:
            if island[next_x][next_y] == 0:
                q.append((start, next_x, next_y, direction, count + 1, False))
            else:
                q.append((start, next_x, next_y, direction, count + 1, True))


# Kruskal
parent: dict = {}
rank: dict = {}
graph: dict = {
    'vertices': [],
    'edges': []
}
def kruskal(graph: dict) -> list:
    def make_set(vertice: int) -> None:
        parent[vertice] = vertice
        rank[vertice] = 0

    def find(vertice: int) -> int:
        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(vertice1: int, vertice2: int) -> None:
        root1: int = find(vertice1)
        root2: int = find(vertice2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]: 
                    rank[root2] += 1

    minimum_spanning_tree: list = []

    for vertice in graph['vertices']:
        make_set(vertice)
        
    edges: list = graph['edges']
    edges.sort(key = lambda x: x[2])
    
    for edge in edges:
        vertice1, vertice2, weight = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)
	    
    return minimum_spanning_tree

island_number: int = 0
for i in range(N):
    for j in range(M):
        if island[i][j] > 0 and is_visited[i][j] == 0:
            island_number += 1
            island[i][j] = island_number
            q.append((island[i][j], i, j, 0, 0, False))
            is_visited[i][j] = 1
            while q:
                start, target_x, target_y, now_direction, now_count, now_met = q.popleft()
                bfs(start, target_x, target_y, now_direction, now_count, now_met)

for i in range(1, island_number + 1):
    graph['vertices'].append(i)

for i in range(N):
    for j in range(M):
        if island[i][j] > 0:
            start: int = island[i][j]
            if 0 <= i - 1 and island[i - 1][j] == 0:
                q.append((island[i][j], i, j, 1, 0, False))
            if i + 1 < N and island[i + 1][j] == 0:
                q.append((island[i][j], i, j, 2, 0, False))
            if 0 <= j - 1 and island[i][j - 1] == 0:
                q.append((island[i][j], i, j, 3, 0, False))
            if j + 1 < M and island[i][j + 1] == 0:
                q.append((island[i][j], i, j, 4, 0, False))

            while q:
                start, target_x, target_y, now_direction, now_count, now_met = q.popleft()
                if now_met:
                    if now_count > 2 and start != island[target_x][target_y]:
                        graph['edges'].append((start, island[target_x][target_y], now_count - 1))
                    continue
                bfs(start, target_x, target_y, now_direction, now_count, now_met)

total: int = 0
result: list = kruskal(graph)
for start, end, cost in result:
    total += cost
print(f'{total}') if len(result) == island_number - 1 else print('-1')