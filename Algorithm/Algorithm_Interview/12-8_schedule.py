from collections import defaultdict

import sys

def solution(n: int, num_list: list) -> bool:
    def dfs(target: int, is_visited: list) -> bool:
        if is_visited[target] == 1:
            return False
        else:
            is_visited[target] = 1
            while course_dict[target]:
                i: int = course_dict[target].pop()
                if not dfs(i, is_visited):
                    return False
            is_visited[target] = 0

        return True
    
    course_dict: defaultdict = defaultdict(list)

    start_index: list = []
    for t in num_list:
        course_dict[t[1]].append(t[0])
        start_index.append(t[1])
    
    for key in start_index:
        print(course_dict)
        if not dfs(key, [0 for _ in range(n)]):
            return False
    return True

print(f'{solution(7, [[1,0], [0,2], [0,3], [0,4], [3,4], [2,3], [5,6], [6, 2], [5, 0], [3, 5]])}')
'''
ex)
    1 <- 0 <- 4
    1 <- 0 <- 3
    1 <- 0 <- 2
    1 <- 0 <- 3 <- 4
    1 <- 0 <- 2 <- 3 <- 4
    5 <- 6 <- 2 <- 3 <- 5 <- 0 (cycle)
'''