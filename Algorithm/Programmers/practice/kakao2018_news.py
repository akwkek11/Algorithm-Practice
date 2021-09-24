from collections import Counter

def solution(str1: str, str2: str) -> int:
    str1_list: list = []
    str2_list: list = []

    for i in range(len(str1) - 1):
        now_target: str = str1[i:i+2]
        if now_target.isalpha():
            str1_list.append(now_target.lower())
    
    for i in range(len(str2) - 1):
        now_target: str = str2[i:i+2]
        if now_target.isalpha():
            str2_list.append(now_target.lower())

    count1: Counter = Counter(str1_list)
    count2: Counter = Counter(str2_list)

    temp_answer: float = 0
    if len(count1) == 0 and len(count2) == 0:
        temp_answer = 1
    
    else:
        intersection: int = len(list((count1 & count2).elements()))
        union: int = len(list((count1 | count2).elements()))
        temp_answer = intersection / union
    
    answer: int = int(temp_answer * 65536)
    return answer

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))