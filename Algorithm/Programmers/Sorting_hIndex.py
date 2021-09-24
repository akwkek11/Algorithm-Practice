import sys

def solution(citations):
    answer: int = 0
    citations.sort()

    if len(citations) <= citations[0]:
        answer = len(citations)
    else:
        for i in range(1, len(citations)):
            index: int = len(citations) - i
            if citations[i] >= index and citations[i-1] <= index:
                answer = index
    return answer

input_list: list = list(map(int, sys.stdin.readline().strip().split()))
print(solution(input_list))