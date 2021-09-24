import sys
sys.setrecursionlimit(10 ** 6)

# Disjoint Set
class DisjointSet:
    def make_set(self, vertice: int) -> list:
        return [i for i in range(vertice + 1)]

    def __init__(self, vertice: int) -> None:
        self.parent: list = self.make_set(vertice + 1)
        self.count: list = [0 for _ in range(vertice + 1)]
        self.group_count: int = 0
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
    
    def counting(self) -> None:
        for i in range(self.size):
            if self.parent[i] == i:
                self.group_count += 1
            self.count[self.find(i)] += 1

N, M = map(int, sys.stdin.readline().strip().split())
disjoint_set: DisjointSet = DisjointSet(N)

for _ in range(M):
    cmd, vertice1, vertice2 = map(int, sys.stdin.readline().strip().split())
    if cmd == 0:
        disjoint_set.union(vertice1, vertice2)
    else:
        print('YES') if disjoint_set.find(vertice1) == disjoint_set.find(vertice2) else print('NO')