from collections import defaultdict

import sys

# Disjoint Set
class DisjointSet:
    def make_set(self, vertice: int) -> list:
        return [i for i in range(vertice + 1)]

    def __init__(self, vertice: int) -> None:
        self.parent: list = self.make_set(vertice + 1)
        self.count: defaultdict = defaultdict(list)
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
    
    def counting(self, cost: list) -> None:
        for i in range(1, self.size + 1):
            if self.parent[i] == i:
                self.group_count += 1
            self.count[self.find(i)].append(cost[i])
        
        for key in self.count.keys():
            self.count[key].sort()

N, M, K = map(int, sys.stdin.readline().strip().split())
disjoint_set: DisjointSet = DisjointSet(N)
cost_list = list(map(int, sys.stdin.readline().strip().split()))
cost_list.insert(0, float('inf'))
for _ in range(M):
    vertice1, vertice2 = map(int, sys.stdin.readline().strip().split())
    disjoint_set.union(vertice1, vertice2)

disjoint_set.counting(cost_list)
total: int = 0
for key, costs in disjoint_set.count.items():
    total += costs[0]

print('Oh no') if total > K else print(f'{total}')