from typing import List
from collections import deque

def solution(rows: int, columns: int, queries: List[List[int]]) -> List[int]:
    rotate_map: List[List[int]] = [[i + j * columns for i in range(1, columns + 1)] for j in range(rows)]
    answer: List[int] = []

    dot_q = deque()
    number_q = deque()
    min_number: int = 0
    for start_x, start_y, end_x, end_y in queries:
        start_x -= 1
        start_y -= 1
        end_x -= 1
        end_y -= 1

        for i in range(start_y, end_y):
            dot_q.append((start_x, i))
            number_q.append(rotate_map[start_x][i])
        for i in range(start_x, end_x):
            dot_q.append((i, end_y))
            number_q.append(rotate_map[i][end_y])
        for i in range(end_y, start_y, -1):
            dot_q.append((end_x, i))
            number_q.append(rotate_map[end_x][i])
        for i in range(end_x, start_x, - 1):
            dot_q.append((i, start_y))
            number_q.append(rotate_map[i][start_y])
        
        number_q.appendleft(number_q.pop())
        min_number = min(list(number_q))
        while dot_q:
            target_x, target_y = dot_q.popleft()
            rotate_map[target_x][target_y] = number_q.popleft()

        answer.append(min_number)
    return answer

print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))