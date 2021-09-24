'''
2021-08-03
'''

def solution(brown: int, yellow: int) -> list:
    '''
        https://programmers.co.kr/learn/courses/30/lessons/42842
    '''
    answer: list = []
    area: int = brown + yellow
    for i in range(3, int(area ** 0.5) + 1):
        if area % i == 0:
            width: int = area // i
            height: int = i
            if (width + height) * 2 - 4 == brown:
                answer.append(width)
                answer.append(height)
                break
    
    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))