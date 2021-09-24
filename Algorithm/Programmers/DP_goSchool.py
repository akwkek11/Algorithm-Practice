def solution(m, n, puddles):
    school_map: list = [[0 for _ in range(m+1)] for _ in range(n+1)]
    is_puddles: list = [[0 for _ in range(m+1)] for _ in range(n+1)]
    answer: int = 0

    for i in puddles:
        is_puddles[i[1]][i[0]] = 1
    school_map[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if not is_puddles[i][j] and (i != 1 or j != 1):
                school_map[i][j] = school_map[i-1][j]%1000000007 + school_map[i][j-1]%1000000007
    print(school_map)
    answer = school_map[n][m]
    return answer

res = solution(4, 3, [[1,2],[2,1]])
print(f'{res}')