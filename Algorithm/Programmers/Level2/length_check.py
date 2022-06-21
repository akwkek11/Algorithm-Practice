from typing import List
from collections import deque

def bfs(x: int, y: int, number: int, count: int, is_visited: List[List[int]], binary_map: List[List[int]], queue: deque) -> bool:
    directions: List[tuple(int, int)] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for step_x, step_y in directions:
        next_x: int = x + step_x
        next_y: int = y + step_y
        if 0 <= next_x < 5 and 0 <= next_y < 5:
            if binary_map[next_x][next_y] == 2 and is_visited[next_x][next_y] != number and count != 0:
                return False
            elif binary_map[next_x][next_y] == 0 and is_visited[next_x][next_y] != number and count != 0:
                is_visited[next_x][next_y] = number
                queue.append((next_x, next_y, number, count - 1))
    return True

def solution(places: List[List[str]]) -> List[int]:
    match_dict: dict[(str, int)] = {'P': 2, 'O': 0, 'X': 1}
    answer: List[bool] = []
    for place in places:
        binary_map: List[List[int]] = [[match_dict[i] for i in place[j]] for j in range(5)]
        is_visited: List[List[int]] = [[0 for _ in range(5)] for _ in range(5)]
        map_index: List[tuple] = [(i, j) for i in range(5) for j in range(5)]
        bfs_queue: deque = deque()
        is_legal: bool = True
        people_count: int = 0
        for i, j in map_index:
            if binary_map[i][j] == 2:
                people_count += 1
                is_visited[i][j] = people_count
                bfs_queue.append((i, j, people_count, 2))
                while bfs_queue:
                    target_x, target_y, number, count = bfs_queue.popleft()
                    if not bfs(target_x, target_y, number, count, is_visited, binary_map, bfs_queue):
                        is_legal = False
                        break

            if not is_legal:
                break
        answer.append(int(is_legal))
    
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))