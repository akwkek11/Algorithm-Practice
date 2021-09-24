import sys

def solution(string: str) -> str:
    def slicing(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return string[left+1: right]
    
    if len(s) < 2 or list(string) == list(reversed(list(string))):
        return string
    
    else:
        result: str = ''
        for i in range(len(string)-1):
            result = max(result, slicing(i, i+1), slicing(i, i+2), key=len)
        return result

s: str = str(sys.stdin.readline().strip())
print(f'{solution(s)}')

'''
ex)
    abdfadafcc -> fadaf
    ccfadafdba
'''