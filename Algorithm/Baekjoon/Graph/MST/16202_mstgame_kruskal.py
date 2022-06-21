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

V, E, step = map(int, sys.stdin.readline().strip().split())
for i in range(1, V + 1):
    graph['vertices'].append(i)

cost: int = 1
for _ in range(E):
    start, end = map(int, sys.stdin.readline().strip().split())
    graph['edges'].append((start, end, cost))
    cost += 1

cannot_create: bool = False
while step:
    total: int = 0
    if not cannot_create:
        result_list = kruskal(graph)
        if len(result_list) != V - 1:
            cannot_create = True
        else:
            for start, end, cost in result_list:
                total += cost
            graph['edges'].remove(result_list[0])

    print(f'{total}', end=' ')
    step -= 1