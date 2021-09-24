import sys

# Disjoint Set
class DisjointSet:
    def make_set(self, vertice: int) -> list:
        return [i for i in range(vertice)]    

    def __init__(self, vertice: int) -> None:
        self.parent: list = self.make_set(vertice)
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

N, M = map(int, sys.stdin.readline().strip().split())
disjoint_set: DisjointSet = DisjointSet(N)

detect_cycle: bool = False
for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    if disjoint_set.find(a) == disjoint_set.find(b):
        print(i + 1)
        detect_cycle = True
        break
    disjoint_set.union(a, b)

if not detect_cycle:
    print('0')