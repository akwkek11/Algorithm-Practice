import re

def solution(files: list) -> list:
    answer: list = []

    head_number_tail: list = [re.split(r"([0-9]+)", file) for file in files]
    sort_head_number_tail: list = sorted(head_number_tail, key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in sort_head_number_tail]

    return answer