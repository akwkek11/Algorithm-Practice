from collections import deque, defaultdict

def solution(land: list, height: int) -> int:
    
    answer: int = 0
    N: int = len(land)
    is_visited: list = [[0 for _ in range(N)] for _ in range(N)]
    bfs_queue: deque = deque(())
    dx: list = [-1, 1, 0, 0]
    dy: list = [0, 0, -1, 1]
    land_marking: int = 1
    
    def land_bfs(x: int, y: int, land_check: int) -> None:
        for i in range(len(dx)):
            next_x: int = x + dx[i]
            next_y: int = y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < N:
                if is_visited[next_x][next_y] == 0 and abs(land[x][y] - land[next_x][next_y]) <= height :
                    is_visited[next_x][next_y] = land_check
                    bfs_queue.append((next_x, next_y, land_check))

        return

    def mst_check(x: int, y: int) -> None:
        for i in range(len(dx)):
            next_x: int = x + dx[i]
            next_y: int = y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < N:
                if is_visited[x][y] != is_visited[next_x][next_y]:
                    start: int = is_visited[x][y]
                    end: int = is_visited[next_x][next_y]
                    graph['edges'][(start, end)] = min(graph['edges'][(start, end)], abs(land[x][y] - land[next_x][next_y]))
                    graph['edges'][(end, start)] = min(graph['edges'][(end, start)], abs(land[x][y] - land[next_x][next_y]))
        return

    # Kruskal
    parent: dict = {}
    rank: dict = {}
    graph: dict = {
        'vertices': [],
        'edges': defaultdict(lambda : float('inf'))
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
            
        edges: list = list(map(list, graph['edges'].items()))
        edges.sort(key = lambda x: x[1])
        
        for edge in edges:
            (vertice1, vertice2), weight = edge
            if find(vertice1) != find(vertice2):
                union(vertice1, vertice2)
                minimum_spanning_tree.append(edge)
            
        return minimum_spanning_tree

    # 1. 구역 나누기
    for i in range(N):
        for j in range(N):
            if is_visited[i][j] == 0:
                is_visited[i][j] = land_marking
                bfs_queue.append((i, j, land_marking))
                land_marking += 1
                while bfs_queue:
                    target_x, target_y, land_number = bfs_queue.popleft()
                    land_bfs(target_x, target_y, land_number)

    # 2. 각 구역마다 최소 비용 저장하기
    for i in range(1, land_marking):
        graph['vertices'].append(i)

    for i in range(N):
        for j in range(N):
            mst_check(i, j)

    # 3. MST 구하기
    for (start, end), cost in kruskal(graph):
        answer += cost
    return answer

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 20))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 9))
print(solution([[1, 10, 100], [100, 1000, 95], [10000, 5000, 2000]], 9))