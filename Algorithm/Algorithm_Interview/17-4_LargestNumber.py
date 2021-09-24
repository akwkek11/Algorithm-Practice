import sys

def solution(num_list: list) -> None:
    size = len(str(max(num_list))) + 1
    numbers = list(map(str, num_list))
    numbers.sort(key=lambda x: x*size, reverse=True)
    print(int(''.join(numbers)))

solution([3, 30, 34, 5, 9])