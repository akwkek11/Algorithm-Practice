def solution(word: list) -> int:
    # 답
    answer: int = 0
    
    # n번째에서 더할 것
    count: dict = {0: 781, 1: 156, 2: 31, 3: 6, 4: 1}
    
    # 각각 모음에 대한 인덱스
    word_dict: dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    '''
        시작이 A인 기준으로
        len(word)
        1 -> 1개
        2 -> 5개
        3 -> 25개
        4 -> 125개
        5 -> 625개

        총 781가지 경우의 수
    '''

    for i in range(len(word)):
        answer += count[i] * word_dict[word[i]] + 1
        
    return answer

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))