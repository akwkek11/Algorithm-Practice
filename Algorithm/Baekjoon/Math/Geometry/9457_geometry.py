import sys

division: int = 10007

def solver() -> list:
    solve_list: list = [[0 for _ in range(2)] for _ in range(50002)]
    solve_list[1][0] = 1
    solve_list[2][0] = 4
    solve_list[2][1] = 3
    for i in range(3, len(solve_list) - 1):
        solve_list[i][0] = ((3*solve_list[i-1][0])%division + solve_list[i-1][1])%division
        solve_list[i][1] = ((2*solve_list[i-1][0])%division + solve_list[i-1][1])%division
    
    return solve_list

answer: list = solver()

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    n: int = int(sys.stdin.readline().strip())
    a = answer[n][0]
    b = ((answer[n][0] + answer[n][1] - 1)*n)%division
    print(f'{a} {b}')