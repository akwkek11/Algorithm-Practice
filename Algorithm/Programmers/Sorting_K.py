def solution(array, commands):
    answer: list = []
    for j in commands:
        temp_list: list = array[j[0]-1:j[1]]
        temp_list.sort()
        answer.append(temp_list[j[2]-1])
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))