def solution(n: int, results: list) -> int:
    def winlose_check(target: int, f_list: list) -> None:
        target_list: list = []
        copy_list: list = []
        for i in range(n):
            if f_list[target - 1][i] == 1:
                target_list.append(i)
            elif f_list[target - 1][i] == -1:
                copy_list.append(i)
        
        for i in target_list:
            for j in copy_list:
                fight_list[i][j] = -1
                fight_list[j][i] = 1
        
        return

    answer: int = 0
    
    fight_list: list = [[0 for _ in range(n)] for _ in range(n)]
    fight_count: list = [0 for _ in range(n)]
    sort_count: list = []
    for i, j in results:
        fight_list[i - 1][j - 1] = 1
        fight_list[j - 1][i - 1] = -1
        fight_count[i - 1] += 1
        fight_count[j - 1] += 1
    
    for i in range(n):
        sort_count.append((i + 1, fight_count[i]))

    sort_count.sort(key = lambda x : x[1], reverse=True)

    # count는 안타깝게도 안쓰이긴 함...
    for index, count in sort_count:
        winlose_check(index, fight_list)

    for i in fight_list:
        if i.count(0) == 1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))