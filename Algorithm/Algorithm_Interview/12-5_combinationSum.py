import sys

def dfs(target: int, start_index: int, now_list: list) -> None:
    for i in range(start_index, len(candidates)):
        if target - candidates[i] >= 0:
            now_list.append(candidates[i])
            if target - candidates[i] > 0:
                dfs(target - candidates[i], i, now_list)
            elif target - candidates[i] == 0:
                now_list.sort()
                if now_list not in result:
                    add_result: list = now_list.copy()
                    result.append(add_result)
            now_list.pop()
        else:
            break

candidates: list = list(map(int, sys.stdin.readline().strip().split()))
target: int = int(sys.stdin.readline().strip())
result: list = []
dfs(target, 0, [])
print(f'{result}')
