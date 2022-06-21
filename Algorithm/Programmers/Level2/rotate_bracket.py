from typing import List

def solution(s: str) -> int:
    answer: int = 0
    is_correct: bool = True
    for i in range(len(s)):
        stack: List[str] = []
        new_s: str = s[i:] + s[:i]
        for word in new_s:
            if word in ['(', '{', '[']:
                stack.append(word)
            else:
                if len(stack) >= 1 and (stack[-1], word) in [('(', ')'), ('{', '}'), ('[', ']')]:
                    stack.pop()
                else:
                    is_correct = False
                    break
        
        if len(stack) != 0:
            is_correct = False
            
        answer += is_correct
        is_correct = True
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))