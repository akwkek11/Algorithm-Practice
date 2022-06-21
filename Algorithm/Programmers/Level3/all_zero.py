import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

answer: int = 0
def solution(a: list, edges: list):
    def dfs(target: int, now_num: int) -> int:
        global answer
        number: int = now_num
        for next in tree_map[target]:
            if is_visited[next] == 0:
                is_visited[next] = 1
                number += dfs(next, a[next])

        answer += abs(number)
        return number

    if sum(a) != 0:
        return -1
    
    is_visited: list = [0 for _ in range(len(a))]
    tree_map: defaultdict = defaultdict(list)
    for i, j in edges:
        tree_map[i].append(j)
        tree_map[j].append(i)

    is_visited[0] = 1
    dfs(0, a[0])
    return answer

print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))
print(solution([-1,-3,-7,11,0],[[0,4],[1,4],[2,4],[3,4]]))