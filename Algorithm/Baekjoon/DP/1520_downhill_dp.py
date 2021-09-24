from collections import deque

import sys
sys.setrecursionlimit(10 ** 5)

def dfs(x: int, y: int) -> int:
    def copy_step_map(now_x: int, now_y: int) -> None:
        is_end_step[now_x][now_y] = 1

        for i in range(len(dx)):
            target_x = now_x + dx[i]
            target_y = now_y + dy[i]
            if 0 <= target_x < M and 0 <= target_y < N and step_map[target_x][target_y] == 1 and is_end_step[target_x][target_y] == 0:
                copy_step_map(target_x, target_y)

    inner_count: int = 0
    step_map[x][y] = 1

    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < M and 0 <= next_y < N and num_map[x][y] > num_map[next_x][next_y] and step_map[next_x][next_y] == 0:
            if is_end_step[next_x][next_y] == 1:
                if final_step[next_x][next_y] == 0:
                    inner_count += 1
                    copy_step_map(x, y)
                else:
                    inner_count += final_step[next_x][next_y]
            elif is_end_step[next_x][next_y] == 0:
                if final_step[next_x][next_y] == 0:
                    inner_count += dfs(next_x, next_y)
                else:
                    inner_count += final_step[next_x][next_y]

    if inner_count == 0:
        is_end_step[x][y] = -1
    step_map[x][y] = 0
    final_step[x][y] = inner_count
    return final_step[x][y]

M, N = map(int, sys.stdin.readline().strip().split())
num_map: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
step_map: list = [[0 for _ in range(N)] for _ in range(M)]
is_end_step: list = [[0 for _ in range(N)] for _ in range(M)]
final_step: list = [[0 for _ in range(N)] for _ in range(M)]
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

is_end_step[M-1][N-1] = 1
count: int = dfs(0, 0)
print(f'{count}')