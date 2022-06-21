def solution(n: int, s: int) -> list:
    if n > s:
        return [-1]
    
    answer: list = [s // n for _ in range(n)]
    end: int = len(answer) - 1
    for i in range(end, end - s%n, -1):
        answer[i] += 1
    return answer

print(solution(4, 9))