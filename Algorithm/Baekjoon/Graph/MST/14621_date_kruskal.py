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

for i in range(1, N + 1):
    graph['vertices'].append(i)

school_type: list = list(map(str, sys.stdin.readline().strip().split()))
school_type.insert(0, '')

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    if school_type[start] != school_type[end]:
        graph['edges'].append((start, end, cost))

total: int = 0
result: list = kruskal(graph)
for start, end, cost in result:
    total += cost

print(f'{total}') if len(result) == N - 1 else print('-1')