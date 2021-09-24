import sys

step_map: list = [[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(100001)]
step_map[0][0][0] = 0

step_list: list = list(map(int, sys.stdin.readline().strip().split()))
step_list.insert(0, 0)
step_index: int = 1

plus_size: list = [1, 3, 4, 3]
while step_list[step_index] != 0:
    command: int = step_list[step_index]
    for i in range(5):
        for j in range(5):
            if i == 0:
                step_map[step_index][command][j] = min(step_map[step_index][command][j], step_map[step_index - 1][i][j] + 2)
                if j != 0:
                    step_map[step_index][i][command] = min(step_map[step_index][i][command], step_map[step_index - 1][i][j] + plus_size[abs(command - j)])
            if j == 0:
                step_map[step_index][i][command] = min(step_map[step_index][i][command], step_map[step_index - 1][i][j] + 2)
                if i != 0:
                    step_map[step_index][command][j] = min(step_map[step_index][command][j], step_map[step_index - 1][i][j] + plus_size[abs(command - i)])
            if i != 0 and j != 0 and i != j:
                step_map[step_index][command][j] = min(step_map[step_index][command][j], step_map[step_index - 1][i][j] + plus_size[abs(command - i)])
                step_map[step_index][i][command] = min(step_map[step_index][i][command], step_map[step_index - 1][i][j] + plus_size[abs(command - j)])
    
    step_index += 1

min_cost: int = float('inf')
for i in range(5):
    for j in range(5):
        min_cost = min(min_cost, step_map[step_index - 1][i][j])

print(min_cost)