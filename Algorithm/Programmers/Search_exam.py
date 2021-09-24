'''
2021-08-03
'''

def solution(answers: list) -> list:
    '''
        https://programmers.co.kr/learn/courses/30/lessons/42840    
    '''
    answer: list = []

    student1: list = [1, 2, 3, 4, 5] * 2000
    student2: list = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    student3: list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    correct_answer: list = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == student1[i]:
            correct_answer[0] += 1
        if answers[i] == student2[i]:
            correct_answer[1] += 1
        if answers[i] == student3[i]:
            correct_answer[2] += 1

    max_correct: int = max(correct_answer)
    for i in range(len(correct_answer)):
        if correct_answer[i] == max_correct:
            answer.append(i + 1)

    answer.sort()
    return answer

print(solution([1,2,3,4,5]))