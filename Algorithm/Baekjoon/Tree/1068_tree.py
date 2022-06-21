from collections import defaultdict

def dfs(start: int) -> int:
    if len(tree_connection_dict[start]) == 0:
        if start in tree_root_list:
            return 0
        return 1
    
    result: int = 0
    is_visited: bool = False
    for end in tree_connection_dict[start]:
        if tree_check[end] == 0:
            is_visited = True
            tree_check[end] = 1
            result += dfs(end)
            tree_check[end] = 0

    if not is_visited:
        return 1
    return result    

tree_check: list = [0 for _ in range(int(input()))]
tree_connect: list = list(map(int, input().split()))
tree_connection_dict: defaultdict = defaultdict(list)
tree_root_list: list = []
for end, start in enumerate(tree_connect):
    if start != -1:
        tree_connection_dict[start].append(end)
    else:
        tree_root_list.append(end)

# 막을 노드
tree_check[int(input())] = 1
result: int = 0
for start in tree_root_list:
    if tree_check[start] == 0:
        result += dfs(start)

print(result)