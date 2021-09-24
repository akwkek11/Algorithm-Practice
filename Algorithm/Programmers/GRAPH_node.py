from collections import defaultdict, deque

def solution(n, edge):
    def bfs(x: int, depth: int) -> None:
        while course[x]:
            next_x: int = course[x].pop()
            if is_visited[next_x] == 0:
                is_visited[next_x] = depth + 1
                q.append((next_x, depth + 1))
    
    course: defaultdict = defaultdict(list)
    for start, end in edge:
        course[start].append(end)
        course[end].append(start)
    
    is_visited: list = [0 for _ in range(n + 1)]
    q: deque = deque(())
    
    q.append((1, 1))
    is_visited[1] = 1
    max_depth: int = -float('inf')
    while q:
        target_vertex, now_depth = q.popleft()
        max_depth = max(max_depth, now_depth)
        bfs(target_vertex, now_depth)

    count: int = 0
    for i in is_visited:
        if i == max_depth:
            count += 1
    return count

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))