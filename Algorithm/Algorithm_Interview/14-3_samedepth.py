def solution(tree_list: list) -> int:
    def dfs(index: int, index_num: int) -> int:
        global res
        left_node: int = 1
        right_node: int = 2
        left: int = 0
        right: int = 0
        if 2 * index + left_node < len(tree_list) and tree_list[2 * index + left_node] != 'null':
            left = dfs(2 * index + left_node, tree_list[2 * index + left_node])
        if 2 * index + right_node < len(tree_list) and tree_list[2 * index + right_node] != 'null':
            right = dfs(2 * index + right_node, tree_list[2 * index + right_node])
        
        if 2 * index + left_node < len(tree_list) and tree_list[2 * index + left_node] == index_num:
            left += 1
        else:
            left = 0
        if 2 * index + right_node < len(tree_list) and tree_list[2 * index + right_node] == index_num:
            right += 1
        else:
            right = 0
        
        res = max(res, left + right)
        return max(left, right)

    start: int = 0
    start_num: int = tree_list[0]
    dfs(start, start_num)
    return res

res: int = 0
print(solution([5, 4, 5, 1, 1, 'null', 5]))
res -= res
print(solution([1, 4, 5, 4, 4, 'null', 5]))
res -= res
print(solution([1, 1, 1, 1, 1, 1, 1, 1]))