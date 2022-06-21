import sys
sys.setrecursionlimit(10 ** 5)

size = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(size)]
right_diagonal = [0 for _ in range(2 * size - 1)]
left_diagonal = [0 for _ in range(2 * size - 1)]
max_black: int = 0
max_white: int = 0

def dfs_black(height: int, width: int, count: int) -> None:
    global max_black
    for i in range(height, size):
        first_start: int = 0
        if i == height:
            first_start = width
        for j in range(first_start, size):
            if (i + j) % 2 == 0 and right_diagonal[i + j] == 0 and left_diagonal[(size - 1) + (i - j)] == 0 and board[i][j] == 1:
                right_diagonal[i + j] = left_diagonal[(size - 1) + (i - j)] = 1
                dfs_black(i, j, count + 1)
                right_diagonal[i + j] = left_diagonal[(size - 1) + (i - j)] = 0
    max_black = max(max_black, count)

def dfs_white(height: int, width: int, count: int) -> None:
    global max_white
    for i in range(height, size):
        first_start: int = 0
        if i == height:
            first_start = width
        for j in range(first_start, size):
            if (i + j) % 2 == 1 and right_diagonal[i + j] == 0 and left_diagonal[(size - 1) + (i - j)] == 0 and board[i][j] == 1:
                right_diagonal[i + j] = left_diagonal[(size - 1) + (i - j)] = 1
                dfs_white(i, j, count + 1)
                right_diagonal[i + j] = left_diagonal[(size - 1) + (i - j)] = 0
    max_white = max(max_white, count)

# 더했을 때 짝수인 케이스
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0 and board[i][j] == 1:
            right_diagonal[i + j] = left_diagonal[(size - 1) + (i - j)] = 1
            dfs_black(i, j, 1)
            right_diagonal[i + j] = left_diagonal[(size - 1) + (i - j)] = 0

# 더했을 때 홀수인 케이스
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 1 and board[i][j] == 1:
            right_diagonal[i + j] = left_diagonal[(size - 1) + (i - j)] = 1
            dfs_white(i, j, 1)
            right_diagonal[i + j] = left_diagonal[(size - 1) + (i - j)] = 0

print(max_black + max_white)