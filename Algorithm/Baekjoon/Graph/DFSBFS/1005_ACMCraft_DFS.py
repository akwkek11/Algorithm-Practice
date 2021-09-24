import sys

sys.setrecursionlimit(10 ** 5)
def DFS(now: int) -> int:
    already_visited[now] = 1

    if not tech_tree[now]:
        cost_map[now] = cost[now]
    else:
        maximum: int = 0
        for i in tech_tree[now]:
            if not already_visited[i]:
                maximum = max(maximum, DFS(i))
            else:
                maximum = max(maximum, cost_map[i])
        cost_map[now] = cost[now] + maximum

    return cost_map[now]

T: int = int(sys.stdin.readline())

for _ in range(T):
    total_cost: int = 0
    N, K = map(int, sys.stdin.readline().split())

    already_visited: list = [0 for _ in range(N + 1)]
    cost: list = [0]
    input_cost: list = list(map(int, sys.stdin.readline().split()))
    cost.extend(input_cost)

    tech_tree: dict = {key : [] for key in range(1, N + 1)}
    cost_map: list = [0 for _ in range(N + 1)]
    for _ in range(K):
        i, j = map(int, sys.stdin.readline().split())
        tech_tree[j].append(i)
    
    target: int = int(sys.stdin.readline())
    total_cost = DFS(target)
    
    print(f'{total_cost}')