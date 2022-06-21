from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

import copy
import heapq
import math
import random
import re
import sys
from typing import Tuple

'''
    주의해줄 것
    1. Pypy에선 전역변수를 '앞'에다 두고, 뒤에 정의된 function에 global을 해줘야 사용이 가능하다.
    2. Python에서의 heapq는 min_heap이다.
    3. bisect_right는 [0, 1, 2, 3, 4] 에서 bisect_right(list, 4)를 했을 시 out of index가 나므로
        - 반드시 len을 벗어났는지 
        - 아니면 return index - 1가 search_target과 같은 값인지 체크해줘야 한다!
'''

'''
    Structure
'''

# Disjoint Set
class DisjointSet:
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

# Trie
class Node(object):
    def __init__(self, key, data=None, count=0):
        self.key = key
        self.data = data
        self.children = {}
        self.count = count
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]

            # len of word
            current_node.count += 1
        current_node.data = string

        # is it end?
        current_node.children['*'] = Node(None)

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words

'''
    Algorithm
'''

# Aho-Corasick
class State:
    sid = None
    value = None
    isFinal = False
    tranList = None
    failState = 0
    outputSet = None

    def __init__(self, sid, val):
        self.sid = sid
        self.value = val
        self.tranList = {}
        self.failState = 0
        self.outputSet = set()

    def goto(self, key):
        if key in self.tranList:
            return self.tranList[key]

    def addOutput(self, key):
        self.outputSet = self.outputSet ^ key

    def display(self):
        print("State:", self.sid, "Outgoing:", len(self.tranList.keys()), "Failure:", self.failState)

        if self.isFinal == True:
            print(" +--Output:", self.outputSet)

        for node in self.tranList.keys():
            s = self.tranList[node]
            s.display()
class AhoCorasick:
    root = None
    sid = 0
    table = {}

    def __init__(self):
        self.root = State(0, None)
        self.table[0] = self.root

    def addKeyword(self, keyword):
        current = self.root

        for key in keyword:
            # print(key)
            if key not in current.tranList:
                self.sid = self.sid + 1
                current.tranList[key] = State(self.sid, key)
                self.table[self.sid] = current.tranList[key]

            current = current.tranList[key]

        current.isFinal = True
        current.outputSet.add(keyword)
    def setFailure(self):
        queue = deque()
        current = self.root

        for k in self.root.tranList:
            queue.append(self.root.tranList[k])

        while len(queue) != 0:
            r = queue.popleft()
            for k in r.tranList:
                queue.append(r.tranList[k])
                nd = r.tranList[k]
                # node = parent's failState
                # goto(node, value)
                sid = r.failState
                value = nd.value
                current = self.table[sid]

                while True:
                    if current.goto(value) == None and current.sid != 0:
                        new_sid = current.failState
                        current = self.table[new_sid]
                    else:
                        break
                child = current.goto(value)

                if child == None:
                    nd.failState = current.sid
                else:
                    nd.failState = child.sid

                nd.addOutput(self.table[nd.failState].outputSet)

    def findString(self, str):
        current = self.root

        for key in str:
            # print("Check:", key)
            while True:
                if current.goto(key) == None and current.sid != 0:
                    current = self.table[current.failState]
                    # print("failure:", current.sid)
                else:
                    child = current.goto(key)
                    break
            if child != None:
                current = child
                '''
                if len(child.outputSet) > 0:
                    print("Sid:", child.sid , child.outputSet)
                '''

    def display(self):
        self.root.display()

# Bellman Ford
def bellman_ford(graph: defaultdict, start: str) -> object:
    distance, predecessor = defaultdict(lambda : float('inf')), defaultdict(lambda : None)
    for node in graph:  
        distance[node]
        predecessor[node]
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    distance[neighbor] = distance[node] + graph[node][neighbor]
                    predecessor[neighbor] = node

    for node in graph:
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                return -1, "Cycle Detected"

    return distance, predecessor

# Bipartite Matching
n, m = 0, 0
visit = [0 for _ in range(n + 1)]
d: list = [0 for i in range(m + 1)]
target_dict: defaultdict = defaultdict(list)
def Bipartite_matching(start: int) -> int:
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in target_dict[start]:
        if d[i] == 0 or Bipartite_matching(d[i]):
            d[i] = start
            return 1
    return 0

# Catalan Number
catalan = lambda n : math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))

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
def meet(p1: tuple, p2: tuple, p3: tuple, p4: tuple) -> tuple:
    if p1 > p2:
        p1, p2 = p2, p1
    if p3 > p4:
        p3, p4 = p4, p3

    if (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]) == 0:
        if p2 == p3:
            return (int(p2[0]), int(p2[1]))
        elif p1 == p4:
            return (int(p1[0]), int(p1[1]))
        else:
            return (-float('inf'), -float('inf'))
    
    else:
        point_x: float = ((p1[0] * p2[1] - p1[1] * p2[0]) * (p3[0] - p4[0]) - (p1[0] - p2[0]) * (p3[0] * p4[1] - p3[1] * p4[0])) / ((p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]))
        point_y: float = ((p1[0] * p2[1] - p1[1] * p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] * p4[1] - p3[1] * p4[0])) / ((p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]))
        return (point_x, point_y)

# Dijsktra
def dijkstra(graph: defaultdict, start: str) -> defaultdict:
    distances: defaultdict = defaultdict(lambda: float('inf'))
    for node in graph:
        distances[node]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance

            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances
    
# Dijsktra with tracing the previous route of target
def dijkstra(graph: defaultdict, start: str, final: str) -> Tuple[defaultdict, list]:
    distances: defaultdict = defaultdict(lambda: float('inf'))
    parents: defaultdict = defaultdict(lambda: float('inf')) 
    for node in graph:
        distances[node]
        parents[node]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance

            if distance < distances[new_destination]:
                distances[new_destination] = distance
                parents[new_destination] = current_destination
                heapq.heappush(queue, [distance, new_destination])
    
    trace: list = [] 
    current: str = final
    is_connected: bool = True
    while current != start: 
        trace.append(current)
        current = parents[current]
        if current == float('inf'):
            is_connected = False
            trace.clear()
            break

    if is_connected:
        trace.append(start)
        trace.reverse()

    # if not connected, return empty list
    return distances, trace

# Euclidean Algorithm - Extend
def ext_euc(a: int, b: int) -> tuple:
    if b == 0:
        return a, 1, 0
    g, x, y = ext_euc(b, a%b)
    return g, y, x-(a//b)*y

# Floyd Warshall (V^3)
def Floyd_Warshall(array: list) -> list:
    cost: list = copy.deepcopy(array)
    for k in range(len(array)):
        cost[k][k] = 0
        for i in range(len(array)):
            for j in range(len(array)):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

    return cost

# Kadane's Algorithm
def kadane(array: list) -> int:
    localMax: int = array[0]
    globalMax: int = array[0]
    for i in range(len(array)):
        localMax = max(array[i], localMax + array[i])
        if localMax > globalMax:
            globalMax = localMax
    
    return globalMax

# KMP
def KMPSearch(target: str, pattern: str) -> list:
    M: int = len(pattern)
    N: int = len(target)

    lps: list = [0 for _ in range(M)]
    result: list = []

    computeLPS(pattern, lps)

    i: int = 0
    j: int = 0
    while i < N:
        if pattern[j] == target[i]:
            i += 1
            j += 1
        elif pattern[j] != target[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == M:
            result.append(i - j + 1)
            j = lps[j - 1]
            
    return result
def computeLPS(pattern: str, lps: list) -> None:
    length: int = 0

    i: int = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Kruskal
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

# Miller-Rabin
def miller_rabin_is_prime(number: int, check_list: list) -> bool:
    odd_num: int = number - 1
    power_of_two: int = 0

    while odd_num % 2 == 0:
        power_of_two += 1
        odd_num //= 2

    for i in check_list:
        checker: int = pow(i,odd_num, number)

        if (checker == 1) or (checker == number - 1):
            continue
        try:
            for loop in range(power_of_two - 1):
                checker = pow(checker,2,number)

                if checker == number - 1:
                    raise TypeError
        except TypeError:
            continue

        return False

    return True

# Pisano Period
def create_map(target: int) -> list:
    fibonacci_map: list = [0, 1, 1]
    while fibonacci_map[len(fibonacci_map) - 2] != 0 or fibonacci_map[len(fibonacci_map) - 1] != 1:
        fibonacci_map.append((fibonacci_map[len(fibonacci_map) - 2] % target + fibonacci_map[len(fibonacci_map) - 1] % target) % target)
    return fibonacci_map

# Pollard-rho
def is_prime(n: int) -> bool:
    alist: list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    
    if n == 1 or n % 2 == 0:
        return False

    if n == 2 or n == 3:
        return True
    
    for a in alist:
        if n == a:
            return True

    if not miller_rabin_is_prime(n, alist):
        return False

    return True
def pollardRho(n: int) -> int:
    def f(x, c):
        return ((x*x % n) + c + n) % n

    if is_prime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2

    x: int = random.randrange(2, n)
    y: int = x

    c: int = random.randrange(1, n)
    d: int = 1

    while d == 1:
        x = f(x, c)
        y = f(f(y, c), c)
        d = math.gcd(abs(x - y), n)
        if d == n:
            return pollardRho(n)

    if is_prime(d):
        return d
    else:
        return pollardRho(d)
        
# Quick Sort
def Quick_Sort(A: list, lo: int, hi: int) -> list:
    def partition(lo: int, hi: int) -> int:
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
    
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        Quick_Sort(A, lo, pivot - 1)
        Quick_Sort(A, pivot + 1, lo)

# Sieve of Eratos
def prime_list(m: int, n: int, mode: int) -> list:
    sieve: list = [True for _ in range(n + 1)] 

    p: int = int(n ** 0.5)
    for i in range(2, p + 1):
        if sieve[i] == True:          
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    # mode == 0 : return T/F Table in range
    if mode == 0:
        return sieve
    # mode == 1 : return var list in range
    elif mode == 1:
        if m == 1 : m = 2
        return [i for i in range(m, n + 1) if sieve[i] == True]