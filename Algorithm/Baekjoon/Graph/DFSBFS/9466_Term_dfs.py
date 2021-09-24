import sys

sys.setrecursionlimit(200000)
T: int = int(sys.stdin.readline().strip())

def dfs(n: int, check_dict: dict, history: list) -> None:
    if check_dict[n]:
        k: int = check_dict[n]
        while k and is_visited[k] == 0 and is_grouped[k] == 0:
            is_grouped[k] = 1
            k = check_dict[k]
        while history:
            is_visited[history.pop()] = 1
    else:
        check_dict[n] = student_list[n]
        #print(f'{n}, {student_list[n]}, {is_visited[n]}')
        history.append(n)
        dfs(student_list[n], check_dict, history)

for _ in range(T):
    n: int = int(sys.stdin.readline().strip())
    student_list: list = [0]
    input_list: list = list(map(int, sys.stdin.readline().strip().split()))
    is_grouped: list = [0 for _ in range(n + 1)]
    is_visited: list = [0 for _ in range(n + 1)]
    student_list.extend(input_list)
    cycle_dict: dict = dict.fromkeys([i for i in range(1, len(student_list))])

    for i in range(1, len(student_list)):
        #print(f'next : {i}')
        if is_visited[i] == 0:
            dfs(i, cycle_dict, [])

    print(f'{len(is_grouped) - 1 - sum(is_grouped)}')