from typing import List
from collections import deque, defaultdict

def solution(rectangle: List[List[int]], characterX: int, characterY: int, itemX: int, itemY: int) -> int:
    max_size: int = 50 + 1
    rectangle_map: List[List[int]] = [[0 for _ in range(max_size + 1)] for _ in range(max_size + 1)]
    is_visited: List[List[int]] = [[0 for _ in range(max_size + 1)] for _ in range(max_size + 1)]
    result_dot: List[List[int]] = [[0 for _ in range(max_size + 1)] for _ in range(max_size + 1)]
    corner_dict: defaultdict(tuple, List[tuple]) = defaultdict(list)

    bfs_queue: deque(tuple(int, int)) = deque()
    directions: List[tuple(int, int)] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 모서리 탐지 BFS, 결과는 result_dot에 저장
    def bfs(x: int, y: int) -> None:
        for i in range(len(directions)):
            next_x: int = x + directions[i][0]
            next_y: int = y + directions[i][1]
            if 0 <= next_x <= max_size and 0 <= next_y <= max_size:
                if not rectangle_map[next_x][next_y]:
                    if i == 0:
                        result_dot[x][y] = result_dot[x][y + 1] = 1
                        corner_dict[(x, y)].append((x, y + 1))
                        corner_dict[(x, y + 1)].append((x, y))
                    elif i == 1:
                        result_dot[x + 1][y] = result_dot[x + 1][y + 1] = 1
                        corner_dict[(x + 1, y)].append((x + 1, y + 1))
                        corner_dict[(x + 1, y + 1)].append((x + 1, y))
                    elif i == 2:
                        result_dot[x][y] = result_dot[x + 1][y] = 1
                        corner_dict[(x, y)].append((x + 1, y))
                        corner_dict[(x + 1, y)].append((x, y))
                    elif i == 3:
                        result_dot[x][y + 1] = result_dot[x + 1][y + 1] = 1
                        corner_dict[(x, y + 1)].append((x + 1, y + 1))
                        corner_dict[(x + 1, y + 1)].append((x, y + 1))

                if not is_visited[next_x][next_y] and rectangle_map[next_x][next_y]:
                    is_visited[next_x][next_y] = 1
                    bfs_queue.append((next_x, next_y))

    # 준비 작업
    for recstart_x, recstart_y, recend_x, recend_y in rectangle:
        for i in range(recstart_x, recend_x):
            for j in range(recstart_y, recend_y):
                rectangle_map[i][j] = 1
    
    # 모서리 점만 추출
    bfs_queue.append((recstart_x, recstart_y))
    is_visited[recstart_x][recstart_y] = 1
    while bfs_queue:
        target_x, target_y = bfs_queue.popleft()
        bfs(target_x, target_y)

    # 최단거리 측정
    bfs_queue.append((characterX, characterY, 0))
    is_visited[characterX][characterY] = 2
    answer: int = float('inf')
    while bfs_queue:
        target_x, target_y, step = bfs_queue.popleft()
        if (target_x, target_y) == (itemX, itemY):
            answer = step
            break
        for next_x, next_y in corner_dict[(target_x, target_y)]:
            if is_visited[next_x][next_y] <= 1 and result_dot[next_x][next_y] == 1:
                is_visited[next_x][next_y] = 2
                bfs_queue.append((next_x, next_y, step + 1))
    return answer

print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 8, 1, 1))
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
print(solution([[1,1,7,5],[6,4,10,10]], 1, 1, 10, 10))