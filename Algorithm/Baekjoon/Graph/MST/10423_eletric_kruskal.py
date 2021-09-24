import sys

parent: dict = {}
rank: dict = {}
graph: dict = {
    'vertices': [],
    'edges': []
}

def kruskal(graph: dict) -> list:
    def make_set(vertice: int) -> None:
        parent[vertice] = -1 if vertice in powerplant else vertice
        rank[vertice] = 0

    def find(vertice: int) -> int:
        if parent[vertice] == -1:
            return -1

        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])

        return parent[vertice]

    def union(vertice1: int, vertice2: int) -> None:
        root1: int = find(vertice1)
        root2: int = find(vertice2)
        if root1 != root2:
            if root1 == -1:
                parent[root2] = root1
            elif root2 == -1:
                parent[root1] = root2
            else:
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

N, M, K = map(int, sys.stdin.readline().strip().split())
powerplant: list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, N + 1):
    graph['vertices'].append(i)

for _ in range(M):
    graph['edges'].append(tuple(map(int, sys.stdin.readline().strip().split())))

total_sum: int = 0
for start, end, cost in kruskal(graph):
    total_sum += cost
print(f'{total_sum}')