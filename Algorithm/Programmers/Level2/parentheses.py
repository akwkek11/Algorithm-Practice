def solution(p: str) -> str:
    def recursion(target: str) -> str:
        if target == '':
            return target
        
        count: int = 0
        u: str = ''
        v: str = ''
        for i in range(2, len(p) + 1, 2):
            u, v = target[:i], target[i:]
            if u.count('(') == len(u) // 2:
                break
        
        correct: bool = True
        for i in u:
            if i == '(':
                count += 1
            else:
                if count == 0:
                    correct = False
                    break
                count -= 1
        
        if correct:
            return u + recursion(v)
        else:
            result: str = '(' + recursion(v) + ')'
            u = u[1:len(u) - 1]
            for i in u:
                if i == '(':
                    result += ')'
                else:
                    result += '('
            return result
            
    answer: str = recursion(p)
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))