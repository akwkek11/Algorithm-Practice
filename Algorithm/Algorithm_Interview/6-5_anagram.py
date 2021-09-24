from collections import defaultdict

def anagram_analysis(str_list: list) -> list:
    res_dict: defaultdict = defaultdict(list)
    for i in str_list:
        key: str = ''.join(sorted(list(i)))
        res_dict[key].append(i)

    print(res_dict)
    res_list: list = []
    for key, value in res_dict.items():
        res_list.append(value)
    
    return res_list

print(anagram_analysis(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

'''
sort는 none을 리턴
sorted가 list 반환

sorted의 key는 func이 될 수 있다.

ex)
    c = ['ccc', 'aaaa', 'd', 'bb']
    sorted(c, key=len) -> ['d', 'bb', 'ccc', 'aaaa']
'''