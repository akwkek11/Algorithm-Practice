def solution(n: int) -> int:
    n_list = [0, 1, 2]
    for i in range(len(n_list) - 1, 2000 + 1):
        n_list.append((n_list[i - 1] + n_list[i]) % 1234567)
    return n_list[n]