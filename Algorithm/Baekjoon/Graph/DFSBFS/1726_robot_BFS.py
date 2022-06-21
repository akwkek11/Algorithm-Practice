from re import L
from typing import List
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())

# 0-1 로봇 맵
# 0 : 길, 1 : 벽, 항상 해답이 존재.
robot_map: List[List[int]] = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
is_visited: List[List[List[List[int]]]] = [[[[0 for _ in range(2)] for _ in range(5)] for _ in range(m)] for _ in range(n)]
queue: deque = deque()

def bfs(x: int, y: int, dir: int, step: int) -> None:
    dx: List[int] = [0, 0, 1, -1]
    dy: List[int] = [1, -1, 0, 0]
    
    # 1. 전진 가능한가?
    if x != end_x or y != end_y:
        for i in range(1, 4):
            next_x: int = x + dx[dir - 1] * i
            next_y: int = y + dy[dir - 1] * i
            if not (0 <= next_x < n and 0 <= next_y < m):
                break
            else:
                if robot_map[next_x][next_y] == 0:
                    if is_visited[next_x][next_y][dir][0] == 0:
                        is_visited[next_x][next_y][dir][0] = 1
                        # print(f"debug, forward : ({next_x, next_y, dir})")
                        queue.append((next_x, next_y, dir, step + 1))
                else:
                    break

    # 2. 방향 회전 Left, right
    # right
    right_list: List[int] = [0, 3, 4, 2, 1]
    if is_visited[x][y][right_list[dir]][1] == 0:
        is_visited[x][y][right_list[dir]][1] = 1
        # print(f"debug, right : ({x, y, right_list[dir]})")
        queue.append((x, y, right_list[dir], step + 1))

    # left
    left_list: List[int] = [0, 4, 3, 1, 2]
    if is_visited[x][y][left_list[dir]][1] == 0:
        is_visited[x][y][left_list[dir]][1] = 1
        # print(f"debug, left : ({x, y, left_list[dir]})")
        queue.append((x, y, left_list[dir], step + 1))


start_x, start_y, start_dir = map(int, sys.stdin.readline().strip().split())
end_x, end_y, end_dir = map(int, sys.stdin.readline().strip().split())
end: tuple = (end_x - 1, end_y - 1, end_dir)
queue.append((start_x - 1, start_y - 1, start_dir, 0))
is_visited[start_x - 1][start_y - 1][start_dir][0] = 1
is_visited[start_x - 1][start_y - 1][start_dir][1] = 1
result: int = 0

while queue:
    now_x, now_y, now_dir, now_step = queue.popleft()
    # print(now_x, now_y, now_dir, now_step)
    if (now_x, now_y, now_dir) == end:
        result = now_step
        break
    bfs(now_x, now_y, now_dir, now_step)

print(result)