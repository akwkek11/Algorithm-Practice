import sys
sys.setrecursionlimit(1000000)

def solve(x: int, y: int) -> int:
    if x == N or y == N:
        return 0
    
    reference: int = dp[x][y]
    if reference != -1:
        return reference
    dp[x][y] = 0

    case1: int = solve(x+1, y)
    case2: int = solve(x+1, y+1)
    case3: int = 0
    if A[x] > B[y]:
        case3 = solve(x, y+1) + B[y]
        
    dp[x][y] = max(case1, case2, case3)
    return dp[x][y]

N: int = int(sys.stdin.readline().strip())
dp: list = [[-1 for _ in range(N)] for _ in range(N)]
A: list = list(map(int, sys.stdin.readline().strip().split()))
B: list = list(map(int, sys.stdin.readline().strip().split()))

print(f'{solve(0, 0)}')