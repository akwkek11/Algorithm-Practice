from collections import defaultdict

def solution(participant, completion):
    answer: str = ''
    sprinter_dict: defaultdict = defaultdict(int)
    for i in participant:
        sprinter_dict[i] += 1
    for i in completion:
        sprinter_dict[i] -= 1
    
    listOfKeys: list = [key for (key, value) in sprinter_dict.items() if value == 1]
    answer = ''.join(listOfKeys)
    return answer

#print(f'{solution(["leo", "kiki", "eden"], ["eden", "kiki"])}')