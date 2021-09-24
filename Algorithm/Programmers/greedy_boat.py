'''
2021-07-27
'''
def solution(people: list, limit: int) -> int:
    '''
        https://programmers.co.kr/learn/courses/30/lessons/42885
    '''
    answer: int = 0
    people.sort()
    start: int = 0
    end: int = len(people) - 1

    while end - start >= 1:
        if people[end] + people[start] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
    
    if start == end:
        answer += 1
    return answer

print(solution([50, 50, 50, 70, 70, 80, 80], 150))
print(solution([50, 50, 50, 70, 70, 80, 80, 80], 150))
print(solution([10, 10, 10, 10, 10], 50))