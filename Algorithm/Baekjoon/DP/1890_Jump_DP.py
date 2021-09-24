import sys

N: int = int(sys.stdin.readline().strip())
jump_map: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
step_map: list = [[0 for _ in range(N)] for _ in range(N)]
is_end_step: list = [[0 for _ in range(N)] for _ in range(N)]
final_step: list = [[0 for _ in range(N)] for _ in range(N)]

is_end_step[N - 1][N - 1] = 1
 
def dfs(x: int, y: int) -> int:
    def copy_step_map(now_x: int, now_y: int) -> None:
        is_end_step[now_x][now_y] = 1

        for i in range(now_x + 1):
            target_x = now_x - i
            if 0 <= target_x < N and step_map[target_x][now_y] == 1 and is_end_step[target_x][now_y] == 0:
                copy_step_map(target_x, now_y)

        for i in range(now_y + 1):
            target_y = now_y - i
            if 0 <= target_y < N and step_map[now_x][target_y] == 1 and is_end_step[now_x][target_y] == 0:
                copy_step_map(now_x, target_y)

    inner_count: int = 0
    step_map[x][y] = 1

    next_x = x + jump_map[x][y]
    if 0 <= next_x < N and step_map[next_x][y] == 0:
        if is_end_step[next_x][y] == 1:
            if final_step[next_x][y] == 0:
                inner_count += 1
                copy_step_map(x, y)
            else:
                inner_count += final_step[next_x][y]
        elif is_end_step[next_x][y] == 0:
            if final_step[next_x][y] == 0:
                inner_count += dfs(next_x, y)
            else:
                inner_count += final_step[next_x][y]

    next_y = y + jump_map[x][y]
    if 0 <= next_y < N and step_map[x][next_y] == 0:
        if is_end_step[x][next_y] == 1:
            if final_step[x][next_y] == 0:
                inner_count += 1
                copy_step_map(x, y)
            else:
                inner_count += final_step[x][next_y]
        elif is_end_step[x][next_y] == 0:
            if final_step[x][next_y] == 0:
                inner_count += dfs(x, next_y)
            else:
                inner_count += final_step[x][next_y]

    if inner_count == 0:
        is_end_step[x][y] = -1
    step_map[x][y] = 0
    final_step[x][y] = inner_count
    return final_step[x][y]

count: int = dfs(0, 0)
print(f'{count}')