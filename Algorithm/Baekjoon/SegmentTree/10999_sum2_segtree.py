import sys

# Segment Tree
'''
    0 : sum
    1 : min
    2 : max
    3 : mul
'''
class SegmentTree:
    def init(self, node: int, left: int, right: int, cmd: int) -> int:
        if left + 1 == right:
            self.tree[node] = self.A[left]
        else:
            mid: int = (left + right) // 2
            if cmd == 0:
                self.tree[node] = self.init(node * 2, left, mid, cmd) + self.init(node * 2 + 1, mid, right, cmd)
            elif cmd == 1:
                self.tree[node] = min(self.init(node * 2, left, mid, cmd), self.init(node * 2 + 1, mid, right, cmd))
            elif cmd == 2:
                self.tree[node] = max(self.init(node * 2, left, mid, cmd), self.init(node * 2 + 1, mid, right, cmd))
            elif cmd == 3:
                self.tree[node] = self.init(node * 2, left, mid, cmd) * self.init(node * 2 + 1, mid, right, cmd)

        return self.tree[node]

    def __init__(self, N: int, A: list, mode: int) -> None:
        self.A = A
        self.tree = [0 for _ in range(4 * N)]
        self.lazy = [0 for _ in range(4 * N)]
        self.mode = mode
        self.init(1, 0, N, mode)

    def lazy_propagation(self, node: int, start: int, end: int) -> None:
        if self.lazy[node]:
            print('aaa')
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0
        return

    def get_sum(self, node: int, left: int, right: int, start: int, end: int) -> int:
        self.lazy_propagation(node, start, end)
        if start <= left and right <= end:
            return self.tree[node]
        if right <= start or end <= left:
            return 0
        mid: int = (left + right) // 2
        return self.get_sum(node * 2, left, mid, start, end) + self.get_sum(node * 2 + 1, mid, right, start, end)

    def get_min(self, node: int, left: int, right: int, start: int, end: int) -> int:
        if start <= left and right <= end:
            return self.tree[node]
        if right <= start or end <= left:
            return float('inf')
        mid: int = (left + right) // 2
        return min(self.get_min(node * 2, left, mid, start, end), self.get_min(node * 2 + 1, mid, right, start, end))

    def get_max(self, node: int, left: int, right: int, start: int, end: int) -> int:
        if start <= left and right <= end:
            return self.tree[node]
        if right <= start or end <= left:
            return -float('inf')
        mid: int = (left + right) // 2
        return max(self.get_max(node * 2, left, mid, start, end), self.get_max(node * 2 + 1, mid, right, start, end))

    def get_mul(self, node: int, left: int, right: int, start: int, end: int) -> int:
        if start <= left and right <= end:
            return self.tree[node]
        if right <= start or end <= left:
            return 1
        mid: int = (left + right) // 2
        return self.get_mul(node * 2, left, mid, start, end) * self.get_mul(node * 2 + 1, mid, right, start, end)

    def query(self, node: int, left: int, right: int, start: int, end: int) -> None:
        funcs: dict = { 0 : self.get_sum,
                        1 : self.get_min,
                        2 : self.get_max,
                        3 : self.get_mul }
        
        func = funcs[self.mode]
        return func(node, left, right, start, end)

    def update_sum(self, node: int, left: int, right: int, target: int, value: int) -> None:
        if target < left or right <= target:
            return self.tree[node]
        
        if left + 1 == right:
            self.tree[node] = value
            return self.tree[node]

        mid = (left + right) // 2
        self.tree[node] = self.update_sum(node * 2, left, mid, target, value) + self.update_sum(node * 2 + 1, mid, right, target, value)
        return self.tree[node]
    
    def update_min(self, node: int, left: int, right: int, target: int, value: int) -> None:
        if target < left or right <= target:
            return self.tree[node]
        
        if left + 1 == right:
            self.tree[node] = value
            return self.tree[node]

        mid = (left + right) // 2
        self.tree[node] = min(self.update_min(node * 2, left, mid, target, value), self.update_min(node * 2 + 1, mid, right, target, value))
        return self.tree[node]

    def update_max(self, node: int, left: int, right: int, target: int, value: int) -> None:
        if target < left or right <= target:
            return self.tree[node]
        
        if left + 1 == right:
            self.tree[node] = value
            return self.tree[node]

        mid = (left + right) // 2
        self.tree[node] = max(self.update_max(node * 2, left, mid, target, value), self.update_max(node * 2 + 1, mid, right, target, value))
        return self.tree[node]

    def update_mul(self, node: int, left: int, right: int, target: int, value: int) -> None:
        if target < left or right <= target:
            return self.tree[node]
        
        if left + 1 == right:
            self.tree[node] = value
            return self.tree[node]
        
        mid = (left + right) // 2
        self.tree[node] = self.update_mul(node * 2, left, mid, target, value) * self.update_mul(node * 2 + 1, mid, right, target, value)
        return self.tree[node]
    
    def update_sum_range(self, node: int, left: int, right: int, start: int, end: int, value: int) -> None:
        self.lazy_propagation(node, start, end)
        if left >= end or right < start:
            return
        
        if left <= start and end <= right:
            self.tree[node] += (end - start + 1) * value
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            return       

        mid = (start + end) // 2
        self.update_sum_range(node * 2, left, right, start, mid, value)
        self.update_sum_range(node * 2 + 1, left, right, mid + 1, end, value)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, node: int, left: int, right: int, start: int, end: int, value: int) -> None:
        funcs_one: dict = { 0 : self.update_sum,
                            1 : self.update_min,
                            2 : self.update_max,
                            3 : self.update_mul }

        funcs_two: dict = { 0 : self.update_sum_range }
        if start == end:
            func = funcs_one[self.mode]
            func(node, left, right, start, value)

        else:
            func = funcs_two[self.mode]
            func(node, left, right, start, end, value)

N, M, K = map(int, sys.stdin.readline().strip().split())
num_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
segTree: SegmentTree = SegmentTree(N, num_list, 0)

for _ in range(M + K):
    cmd: list = list(map(int, sys.stdin.readline().strip().split()))
    cmd[1] -= 1

    if cmd[0] == 2:
        print(f'{segTree.query(1, 0, N, cmd[1], cmd[2])}')
    
    else:
        segTree.update(1, 0, N, cmd[1], cmd[2], cmd[3])