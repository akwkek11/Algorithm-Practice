def solution(n: int, left: int, right: int) -> list:
    real_left = int(left)
    real_right = int(right)

    left_index: int = real_left // n
    left_start: int = real_left % n
    right_index: int = real_right // n
    right_end: int = n * (right_index - left_index) + (real_right % n)
    answer: list = []

    for i in range(left_index, right_index + 1):
        answer.extend([max(i + 1, j) for j in range(1, n + 1)])
    
    return answer[left_start:right_end + 1]