import sys

parent: dict = {}
rank: dict = {}
graph: dict = {
    'vertices': [],
    'edges': []
}

# mode : 0 -> min, 1 -> max
def kruskal(graph: dict, mode: int) -> list:
    def make_set(vertice: int) -> None:
        parent[vertice] = vertice
        rank[vertice] = 0

    def find(vertice: int) -> int:
        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(vertice1: int, vertice2: int) -> None:
        root1 = find(vertice1)
        root2 = find(vertice2)
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
    edges.sort(key = lambda x: x[2]) if mode == 0 else edges.sort(key = lambda x: x[2], reverse = True)
    
    for edge in edges:
        vertice1, vertice2, weight = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)
	    
    return minimum_spanning_tree

N, M = map(int, sys.stdin.readline().strip().split())

for i in range(N + 1):
    graph['vertices'].append(i)

for _ in range(M + 1):
    graph['edges'].append(tuple(map(int, sys.stdin.readline().strip().split())))

# minimum이 오르막길 최대
max_sum: int = 0
for start, end, cost in kruskal(graph, 0):
    if cost == 0:
        max_sum += 1

# 반대로, maximum이 내리막길 최대
min_sum: int = 0
for start, end, cost in kruskal(graph, 1):
    if cost == 0:
        min_sum += 1

print(f'{max_sum ** 2 - min_sum ** 2}')