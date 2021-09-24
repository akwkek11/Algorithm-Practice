from collections import deque

def solution(m: int, n: int, board: list):
    def bfs(x: int, y: int) -> None:
        count: int = 0
        for i in range(len(dx)):
            next_x: int = x + dx[i]
            next_y: int = y + dy[i]
            if 0 <= next_x < m and 0 <= next_y < n and visited[next_x][next_y] == 0 and new_board[x][y] == new_board[next_x][next_y]:
                count += 1
            else:
                break

        if count == 3:
            st.append((x, y))
            for i in range(len(dx)):
                st.append((x + dx[i], y + dy[i]))
    def down():
        for y in range(n):
            status = deque([])
            for x in range(m - 1, -1, -1):
                if new_board[x][y] != '.':
                    status.append(new_board[x][y])
            for x in range(m - 1, -1, -1):
                if status:
                    new_board[x][y] = status.popleft()
                else:
                    new_board[x][y] = '.'
    
    visited: list = [[0 for _ in range(n)] for _ in range(m)]
    is_vaild: bool = False
    answer: int = 0
    dx: list = [0, 1, 1]
    dy: list = [1, 0, 1]
    
    new_board: list = []
    for block_line in board:
        new_board.append(list(block_line))

    while True:
        st: deque = deque(())
        for i in range(m):
            for j in range(n):
                if new_board[i][j] != '.' and visited[i][j] == 0:
                    visited[i][j] = 1
                    q = deque()
                    q.append((i, j))
                    while q:
                        now = q.popleft()
                        bfs(now[0], now[1])

        if len(st) >= 4:
            is_vaild = True
            for s in st:
                if new_board[s[0]][s[1]] != '.':
                    answer += 1
                new_board[s[0]][s[1]] = '.'
        '''
        for i in range(m):
            for j in range(n):
                print(new_board[i][j], end = ' ') if j != n - 1 else print(new_board[i][j])
        print()
        '''
        down()
        '''
        for i in range(m):
            for j in range(n):
                print(new_board[i][j], end = ' ') if j != n - 1 else print(new_board[i][j])
        '''
        if not is_vaild:
            break

        is_vaild = False
        for i in range(m):
            for j in range(n):
                visited[i][j] = 0
    
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))