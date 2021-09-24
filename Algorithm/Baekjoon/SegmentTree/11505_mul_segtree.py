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
        self.mode = mode
        self.init(1, 0, N, mode)

    def get_sum(self, node: int, left: int, right: int, start: int, end: int) -> int:
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
    
    def update(self, node: int, left: int, right: int, target: int, value: int) -> None:
        funcs: dict = { 0 : self.update_sum,
                        1 : self.update_min,
                        2 : self.update_max,
                        3 : self.update_mul }
        
        func = funcs[self.mode]
        func(node, left, right, target, value)

N, M, K = map(int, sys.stdin.readline().strip().split())
num_list: list = [int(sys.stdin.readline().strip()) for _ in range(N)]
segment_min_tree: SegmentTree = SegmentTree(N, num_list, 1)
segment_max_tree: SegmentTree = SegmentTree(N, num_list, 2)
segment_tree: SegmentTree = SegmentTree(N, num_list, 3)

for _ in range(M + K):
    cmd, a, b = map(int, sys.stdin.readline().strip().split())
    a -= 1

    if cmd == 2:
        print(f'mul : {segment_tree.query(1, 0, N, a, b)}')
        print(f'min : {segment_min_tree.query(1, 0, N, a, b)}')
        print(f'max : {segment_max_tree.query(1, 0, N, a, b)}')
    
    else:
        segment_tree.update_mul(1, 0, N, a, b)
        segment_min_tree.update_min(1, 0, N, a, b)
        segment_max_tree.update_max(1, 0, N, a, b)
        segment_tree.A[a] = b