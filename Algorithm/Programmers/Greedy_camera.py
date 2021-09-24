def solution(routes):
    sort_routes: list = sorted(routes, key=lambda x: x[1])
    print(sort_routes)
    answer: int = 0

    end: int = -float('inf')
    for i in sort_routes:
        if i[0] > end:
            end = i[1]
            answer += 1

    return answer

print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))