'''
2021-07-27
'''
import string

def solution(name: str) -> int:
    '''
        https://programmers.co.kr/learn/courses/30/lessons/42860
    '''
    answer: int = 0
    diff: list = []
    for index, value in enumerate(name):
        if value != 'A':
            diff.append(index)

    if len(diff) == 0:
        return 0
    alpha_dict: dict = dict(zip(string.ascii_uppercase, range(1, 27)))

    for i in diff:
        answer += min(27 - alpha_dict[name[i]], alpha_dict[name[i]] - 1)

    # 전부 -> 로만 진행했을 경우
    min_move: int = diff[-1]
    if diff[0] != 0:
        diff.insert(0, 0)
    for i in range(len(diff) - 1):
        min_move = min(min_move, diff[i] * 2 + len(name) - diff[i + 1])

    answer += min_move
    return answer

print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JAZ"))
print(solution("ABABAAAAAAABA"))
print(solution("AAZ"))
print(solution("BBBAAB"))
print(solution("AABAAAAAAABBB"))
print(solution("ABAAAAAAAAABB"))