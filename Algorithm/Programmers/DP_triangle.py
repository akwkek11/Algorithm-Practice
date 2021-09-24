res_table: list = [[0 for _ in range(501)] for _ in range(501)]

def solution(triangle):
    answer: int = 0
    count: int = 0
    for i in range(len(triangle)-1, -1, -1):
        for j in triangle[i]:
            if i == len(triangle)-1:
                res_table[i][count] = j
            else:
                res_table[i][count] = max(res_table[i+1][count], res_table[i+1][count+1]) + j
            count += 1
            if count == i+1:
                break
        count = 0
    
    answer = res_table[0][0]
    return answer

triangle: list = [[7, 0, 0, 0, 0], [3, 8, 0, 0, 0], [8, 1, 0, 0, 0], [2, 7, 4, 4, 0], [4, 5, 2, 6, 5]]
res = solution(triangle)

print(res_table)
print(f'{res}')

'''
def solution(triangle):
    answer: int = 0
    count: int = 0
    for i in range(len(triangle)):
        for j in triangle[i]:
            if i == 0:
                res_table[i][count] = j
            else:
                if not count or i == count:
                    res_table[i][count] = res_table[i-1][count] + j
                else:
                    res_table[i][count] = max(res_table[i-1][count-1], res_table[i-1][count]) + j
            count += 1
            if count == i+1:
                break
        count = 0
        for k in range(0, i+1):
            answer = max(answer, res_table[i][k])

    return answer
'''