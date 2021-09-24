import sys

# CCW
def ccw(p1: tuple, p2: tuple, p3: tuple) -> int:
    op: int = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    op -= p1[0] * p3[1] + p2[0] * p1[1] + p3[0] * p2[1]

    if op > 0:
        return 1
    
    elif op == 0:
        return 0

    else:
        return -1
def check_intersection(p1: tuple, p2: tuple, p3: tuple, p4: tuple) -> bool:

    ab: int = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    cd: int = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    if ab == 0 and cd == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        
        return (p1 <= p4 and p3 <= p2)

    return (ab <= 0 and cd <= 0)

# disjoint_set
class disjoint_set:
    def make_set(self, vertice: int) -> list:
        return [i for i in range(vertice)]    

    def __init__(self, vertice: int) -> None:
        self.parent: list = self.make_set(vertice)
        self.count: list = [0 for _ in range(vertice)]
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
line_group: disjoint_set = disjoint_set(N)
line_list: list = []

for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    line_list.append(((x1, y1), (x2, y2)))

for i in range(N):
    for j in range(i + 1, N):
        if check_intersection(line_list[i][0], line_list[i][1], line_list[j][0], line_list[j][1]):
            line_group.union(i, j)

line_group.counting()
print(f'{line_group.group_count}')
print(f'{max(line_group.count)}')