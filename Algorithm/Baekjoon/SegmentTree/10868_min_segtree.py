import sys

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

    def sum(self, node: int, left: int, right: int, start: int, end: int) -> int:
        if start <= left and right <= end:
            return self.tree[node]
        if right <= start or end <= left:
            return 0
        mid: int = (left + right) // 2
        return self.sum(node * 2, left, mid, start, end) + self.sum(node * 2 + 1, mid, right, start, end)

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

    def mul(self, node: int, left: int, right: int, start: int, end: int) -> int:
        if start <= left and right <= end:
            return self.tree[node]
        if right <= start or end <= left:
            return 1
        mid: int = (left + right) // 2
        return self.mul(node * 2, left, mid, start, end) * self.mul(node * 2 + 1, mid, right, start, end)

    def update(self, node: int, left: int, right: int, target: int, value: int) -> None:
        if left <= target < right:
            self.tree[node] += value
            if left + 1 == right:
                return

            mid = (left + right) // 2
            self.update(node * 2, left, mid, target, value)
            self.update(node * 2 + 1, mid, right, target, value)

N, M = map(int, sys.stdin.readline().strip().split())
num_list: list = [int(sys.stdin.readline().strip()) for _ in range(N)]
segment_min_tree: SegmentTree = SegmentTree(N, num_list, 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    a -= 1
    print(f'{segment_min_tree.get_min(1, 0, N, a, b)}')