from collections import defaultdict

import sys

# Disjoint Set
class DisjointSet:
    def make_set(self, vertice: int) -> list:
        return [i for i in range(vertice)]    

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

N: int = int(sys.stdin.readline().strip())
M: int = int(sys.stdin.readline().strip())

disjoint_set: DisjointSet = DisjointSet(N)

for i in range(1, N + 1):
    connect: list = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(N):
        if connect[j] == 1:
            disjoint_set.union(i, j + 1)

travel_list: list = list(map(int, sys.stdin.readline().strip().split()))
travel_connect_dict: defaultdict = defaultdict(int)
for i in travel_list:
    travel_connect_dict[disjoint_set.find(i)] = 1

print('YES') if len(travel_connect_dict) == 1 else print('NO')