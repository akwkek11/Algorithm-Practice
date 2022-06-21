from collections import deque
from typing import Deque

def solution(maps: list) -> int:
    def bfs(target_n: int, target_m: int) -> None:
        directions: list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in directions:
            if (target_n + x >= 0 and target_n + x < n) and (target_m + y >= 0 and target_m + y < m):
                if maps[target_n + x][target_m + y] == 1 and check_list[target_n + x][target_m + y] == 0:
                    check_list[target_n + x][target_m + y] = check_list[target_n][target_m] + 1
                    bfs_queue.append((target_n + x, target_m + y))

    n: int = len(maps)
    m: int = len(maps[0])
    check_list: list = [[0 for _ in range(m)] for _ in range(n)]
    bfs_queue: deque = deque()
    bfs_queue.append((0, 0))
    check_list[0][0] = 1
    answer: int = -1

    while bfs_queue:
        now_n, now_m = bfs_queue.popleft()
        if now_n + 1 == n and now_m + 1 == m:
            answer = check_list[now_n][now_m]
            break
        bfs(now_n, now_m)
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))