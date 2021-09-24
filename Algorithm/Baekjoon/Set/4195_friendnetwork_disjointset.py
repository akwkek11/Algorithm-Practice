from collections import defaultdict

import sys

# Disjoint Set
class DisjointSet:
    def __init__(self) -> None:
        self.parent: defaultdict = defaultdict(str)
        self.count: defaultdict = defaultdict(int)
        self.group_count: int = 0
        
    def find(self, vertice: str) -> str:
        if self.parent[vertice] != vertice:
            self.parent[vertice] = self.find(self.parent[vertice])

        return self.parent[vertice]

    def union(self, vertice1: str, vertice2: str) -> None:
        if self.parent[vertice1] == '':
            self.parent[vertice1] = vertice1
            self.count[vertice1] = 1

        if self.parent[vertice2] == '':
            self.parent[vertice2] = vertice2
            self.count[vertice2] = 1
        
        root1: int = self.find(vertice1)
        root2: int = self.find(vertice2)
        if root1 != root2:
            self.parent[root2] = root1
            self.count[root1] += self.count[root2]
    
    def counting(self, vertice: str) -> int:
        return self.count[vertice]

T: int = int(sys.stdin.readline().strip())
for _ in range(T):
    N: int = int(sys.stdin.readline().strip())
    disjoint_set: DisjointSet = DisjointSet()
    for i in range(N):
        a, b = map(str, sys.stdin.readline().strip().split())

        disjoint_set.union(a, b)
        print(disjoint_set.counting(disjoint_set.find(a)))