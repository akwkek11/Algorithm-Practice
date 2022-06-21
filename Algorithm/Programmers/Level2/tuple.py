from collections import defaultdict

def solution(s : str) -> list:
    answer: list = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=lambda x: len(x))

    check_list: defaultdict = defaultdict(int)
    for target in s:
        target_list = target.split(',')
        for i in target_list:
            if check_list[i] == 0:
                check_list[i] = 1
                answer.append(int(i))
                break
            
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))