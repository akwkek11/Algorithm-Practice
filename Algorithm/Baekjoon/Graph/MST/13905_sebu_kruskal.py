import sys

# Kruskal
parent: dict = {}
rank: dict = {}
graph: dict = {
    'vertices': [],
    'edges': []
}
def find(vertice: int) -> int:
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def kruskal(graph: dict, start: int, end: int) -> list:
    def make_set(vertice: int) -> None:
        parent[vertice] = vertice
        rank[vertice] = 0

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

    maximum_spanning_tree: list = []

    for vertice in graph['vertices']:
        make_set(vertice)
        
    edges: list = graph['edges']
    edges.sort(key = lambda x: x[2], reverse=True)
    
    for edge in edges:
        vertice1, vertice2, weight = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            maximum_spanning_tree.append(edge)

        if find(start) == find(end):
            return maximum_spanning_tree
	    
    return maximum_spanning_tree

N, M = map(int, sys.stdin.readline().strip().split())
start, end = map(int, sys.stdin.readline().strip().split())
for i in range(1, N + 1):
    graph['vertices'].append(i)
for _ in range(M):
    graph['edges'].append(tuple(map(int, sys.stdin.readline().strip().split())))

results: list = kruskal(graph, start, end)
if find(start) == find(end):
    print(results[-1][2])
else:
    print(0)