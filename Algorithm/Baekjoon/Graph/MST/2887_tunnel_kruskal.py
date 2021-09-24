import sys

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

N: int = int(sys.stdin.readline().strip())
for i in range(N):
    graph['vertices'].append(i)
star_list: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
for i in range(len(star_list)):
    star_list[i].append(i)

total_sum: int = 0
for i in range(3):
    star_list.sort(key = lambda x : x[i])
    for j in range(N - 1):
        graph['edges'].append((star_list[j][3], star_list[j + 1][3], star_list[j + 1][i] - star_list[j][i]))

for start, end, cost in kruskal(graph):
    total_sum += cost

print(f'{total_sum}')