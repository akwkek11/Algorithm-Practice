import re

def solution(new_id):
    # 스탭 1. 소문자
    new_id = new_id.lower()

    # 스탭 2. 특수문자 제거
    new_id = re.sub(r"[^a-zA-Z0-9.\-\_]", "", new_id)

    # 스탭 3. 마침표 여러개인 경우
    new_id = re.sub('(([.])\\2{1,})', '.', new_id)

    # 스탭 4. 처음과 끝이 마침표라면 제거
    start: int = 0
    end: int = len(new_id)
    if len(new_id) != 0:
        if new_id[start] == '.':
            start = 1
        
        if new_id[-1] == '.':
            end -= 1
        new_id = new_id[start: end]

    # 스탭 5. 만약 빈 문자열이라면?
    if new_id == '':
        new_id = 'a'

    # 스탭 6. 문자열 슬라이싱
    new_id = new_id[0: 15]
    if new_id[-1] == '.':
        new_id = new_id[0: 14]

    # 스탭 7. 문자열 개수가 2자 이하면?
    add_id = new_id[-1]
    while len(new_id) < 3:
        new_id = new_id + add_id

    return new_id

print(solution("123_.def"))