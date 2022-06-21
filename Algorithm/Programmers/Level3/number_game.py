def solution(A: list, B: list) -> int:
    A.sort()
    B.sort()
    answer: int = 0

    for i in range(len(B) - 1, -1, -1):
        if B[-1] > A[i]:
            answer += 1
            B.pop()
            
    return answer