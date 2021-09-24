from collections import defaultdict, deque

import copy
import sys

def solution(n: int, edges: list) -> list:
    def bfs(x: int, depth: int) -> None:
        for i in node_dict[x]:
            if is_visited[i] == 0:
                is_visited[i] = 1
                q.append((i, depth + 1))        
        return
    
    is_visited: list = [0 for _ in range(n+1)]
    is_visited_init: list = [0 for _ in range(n+1)]
    node_dict: defaultdict = defaultdict(list)

    for start, end in edges:
        node_dict[start].append(end)
        node_dict[end].append(start)

    key_list: list = list(node_dict.keys())

    depth_result: list = []
    q: deque = deque()
    for i in key_list:
        is_visited[i] = 1
        q.append((i, 0))
        max_depth = 0
        while q:
            target, now_depth = q.popleft()
            max_depth = max(max_depth, now_depth)
            bfs(target, now_depth)
        depth_result.append((i, max_depth))
        is_visited = copy.deepcopy(is_visited_init)

    depth_result.sort(key=lambda x : x[1], reverse = True)
    min_depth: int = depth_result[-1][1]
    res_list: list = []
    while True:
        x, dep = depth_result.pop()
        if min_depth < dep:
            break
        else:
            res_list.append(x)
    
    res_list.sort()
    return res_list

print(f'{solution(6, [[0,3], [1,3], [2,3], [4,3], [5,4]])}')
print(f'{solution(4, [[1,0], [1,2], [1,3]])}')