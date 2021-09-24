from collections import defaultdict

def solution(msg: str) -> list:
    answer: list = []
    alpha_dict: defaultdict = defaultdict(int)
    last_index: int = 1
    for i in [chr(i) for i in range(65, 65 + 26)]:
        alpha_dict[i] = last_index
        last_index += 1
    
    start: int = 0
    end: int = start + 1
    while start < len(msg):
        index_num: int = 0
        while True:
            target: str = msg[start:end]
            if end > len(msg):
                break

            if alpha_dict[target] >= 1:
                index_num = alpha_dict[target]
                end += 1
            else:
                alpha_dict[target] = last_index
                last_index += 1
                break
        
        answer.append(index_num)
        start = end - 1
        end = start + 1
    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))