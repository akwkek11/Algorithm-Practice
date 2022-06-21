from typing import List
from collections import Counter

def solution(s: str) -> int:
    answer: int = float('inf')
    if len(s) == 1:
        return 1

    for divisor in range(1, len(s) // 2 + 1):
        divide_list: List[str] = [s[divisor * i: divisor * (i + 1)] for i in range(len(s) // divisor)]
        result_length: int = len(s)
        result_data: List[(tuple(int, int))] = []
        count: int = 1
        compare_string: str = ''
        for i in range(len(divide_list) - 1):
            compare_string = divide_list[i]
            if compare_string == divide_list[i + 1]:
                count += 1
            else:
                result_data.append((len(compare_string), count))
                count = 1
        result_data.append((len(compare_string), count))
        for string_length, count in result_data:
            if count > 1:
                result_length -= string_length * (count - 1) - len(str(count))
        answer = min(answer, result_length)
    
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution('a'))
print(solution('aa'))
print(solution('ab'))
print(solution('abcabc'))
print(solution('abcabcabcabfabcabdabcabe'))
print(solution('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'))