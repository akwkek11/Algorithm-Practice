import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x: int) -> None:
    check[x] = 1
    for i in range(N):
        if check[i] != 1 and adj[x][i]:
            dfs(i)
    answer.append(x + 1)

N: int = int(sys.stdin.readline().strip())
check: list = [0 for _ in range(N)]
answer: list = []
adj: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dfs(0)

answer = answer[::-1]
print(len(answer))
print(' '.join([str(i) for i in answer]))