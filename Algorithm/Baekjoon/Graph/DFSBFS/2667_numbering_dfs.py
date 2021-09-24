import sys

n: int = int(sys.stdin.readline().strip())
home_map: list = []
visited: list = [[0 for _ in range(n)] for _ in range(n)]
count: int = 0
home_size: list = []
size: int = 0

def dfs(x, y):
    global home_map
    global visited
    global size
    dx: list = [-1, 1, 0, 0]
    dy: list = [0, 0, -1, 1]

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n and home_map[next_x][next_y] == '1' and visited[next_x][next_y] == 0:
            visited[next_x][next_y] = 1
            size += 1
            dfs(next_x, next_y)

for i in range(n):
    home_map.append(str(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(n):
        if home_map[i][j] == '1' and visited[i][j] == 0:
            visited[i][j] = 1

            size = 1
            count += 1

            dfs(i, j)

            home_size.append(size)
            size = 0

home_size.sort()
print(f'{count}')
for i in home_size:
    print(f'{i}')