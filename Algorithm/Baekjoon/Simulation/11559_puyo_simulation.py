from collections import deque

board: list = []
for _ in range(12):
    board.append(list(input()))

visited: list = [[0 for _ in range(6)] for _ in range(12)]
is_vaild: bool = 0
answer: int = 0

def BFS(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for direction in range(len(dx)):
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        if 0 <= next_x < 12 and 0 <= next_y < 6:
            if board[x][y] == board[next_x][next_y] and visited[next_x][next_y] == 0:
                q.append([next_x, next_y])
                visited[next_x][next_y] = 1
def down():
    for y in range(6):
        status = deque([])
        for x in range(11, -1, -1):
            if board[x][y] != '.':
                status.append(board[x][y])
        for x in range(11, -1, -1):
            if status:
                board[x][y] = status.popleft()
            else:
                board[x][y] = '.'

while True:
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                q = deque([[i, j]])
                st = []
                while q:
                    now = q.popleft()
                    st.append(now)
                    BFS(now[0], now[1])
                if len(st) >= 4:
                    is_vaild = True
                    for s in st:
                        board[s[0]][s[1]] = '.'
    down()
    if not is_vaild:
        break
    is_vaild = False
    answer += 1
    for i in range(12):
        for j in range(6):
            visited[i][j] = 0
print(answer)