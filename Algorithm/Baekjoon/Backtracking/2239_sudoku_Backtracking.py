import sys

check_square = lambda x, y: (x // 3) * 3 + (y // 3)

def DFS(start: int) -> bool:
    if start == 81:
        for i in range(9):
            for j in range(9):
                print(f'{sudoku[i][j]}', end = '') if j != 8 else print(f'{sudoku[i][j]}')

        return True

    x: int = start // len(sudoku)
    y: int = start % len(sudoku)

    if sudoku[x][y] != 0:
        return DFS(start + 1)
    else:
        for i in range(1, 10):
            if not check1[x][i] and not check2[y][i] and not check3[check_square(x, y)][i]:
                check1[x][i] = check2[y][i] = check3[check_square(x, y)][i] = True
                sudoku[x][y] = i
                if DFS(start + 1):
                    return True
                sudoku[x][y] = 0
                check1[x][i] = check2[y][i] = check3[check_square(x, y)][i] = False
    
    return False

sudoku: list = [list(map(int, list(str(sys.stdin.readline().strip())))) for _ in range(9)]
check1: list = [[False for _ in range(10)] for _ in range(10)]
check2: list = [[False for _ in range(10)] for _ in range(10)]
check3: list = [[False for _ in range(10)] for _ in range(10)]

for i in range(9):
    for j in range(9):
        check1[i][sudoku[i][j]] = True
        check2[j][sudoku[i][j]] = True
        check3[check_square(i, j)][sudoku[i][j]] = True

DFS(0)
