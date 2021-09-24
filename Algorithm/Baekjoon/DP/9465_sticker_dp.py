import sys

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    n: int = int(sys.stdin.readline().strip())
    num_list: list = [[0, 0] for i in range(2)]
    res_list: list = [[0 for _ in range(n + 2)] for _ in range(2)]
    for i in range(2):
        num_list[i].extend(list(map(int, sys.stdin.readline().strip().split())))

    for i in range(2, n + 2):
        res_list[0][i] = max(res_list[1][i - 2], res_list[1][i - 1]) + num_list[0][i]
        res_list[1][i] = max(res_list[0][i - 2], res_list[0][i - 1]) + num_list[1][i]

    max_res: int = max(res_list[0][n + 1], res_list[1][n + 1])
    print(f'{max_res}')