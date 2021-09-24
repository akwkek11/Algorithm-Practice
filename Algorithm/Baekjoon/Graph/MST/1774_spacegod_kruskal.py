import sys

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

N, M = map(int, sys.stdin.readline().strip().split())
star_list: list = []

for i in range(1, N + 1):
    graph['vertices'].append(i)

for i in range(N):
    x, y = map(float, sys.stdin.readline().strip().split())
    star_list.append((x, y))
    if i != 0:
        for index, point in enumerate(star_list):
            graph['edges'].append((index + 1, i + 1, ((point[0] - x) ** 2 + (point[1] - y) ** 2) ** 0.5 ))

for i in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    graph['edges'].append((start, end, 0))

total: float = 0
for start, end, cost in kruskal(graph):
    total += cost
print(f'{format(round(total, 2), ".2f")}')