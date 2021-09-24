from collections import defaultdict
# from itertools import combinations

def solution(clothes):
    answer = 1
    spy_dict: defaultdict = defaultdict(list)
    leng_value: list = []

    temp: int = 0

    for i in clothes:
        spy_dict[i[1]].append(i[0])
    
    for key, value in spy_dict.items():
        leng_value.append(len(spy_dict[key]))
    
    '''
    for i in range(1, len(leng_value)+1):
        combination = list(combinations(leng_value, i))
        for j in combination:
            for k in j:
                if i == 1:
                    temp = k
                else:
                    temp *= k
            
            answer += temp
            temp = 1
    '''

    if len(leng_value) == 0:
        answer = 0
    else:
        for i in leng_value:
            answer *= (i + 1)
        answer -= 1
    return answer