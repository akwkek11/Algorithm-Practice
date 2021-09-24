import sys

def dfs(now_str: list, index: int) -> None:
    for i in num_dict[input_num[index]]:
        now_str.append(i)
        dfs_result.append(''.join(now_str)) if index == len(input_num) - 1 else dfs(now_str, index + 1)
        now_str.pop()
    return

num_dict: dict = {2: ['a', 'b', 'c'],
                  3: ['d', 'e', 'f'],
                  4: ['g', 'h', 'i'],
                  5: ['j', 'k', 'l'],
                  6: ['m', 'n', 'o'],
                  7: ['p', 'q', 'r', 's'],
                  8: ['t', 'u', 'v'],
                  9: ['w', 'x', 'y', 'z']}

input_num: list = list(map(int, list(str(sys.stdin.readline().strip()))))
dfs_result: list = []
dfs([], 0)

print(f'{dfs_result}')