import sys

from collections import deque

n, m, k = map(int, sys.stdin.readline().strip().split())
food_map: list = [[0 for _ in range(m)] for _ in range(n)]
visited: list = [[0 for _ in range(m)] for _ in range(n)]
dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]
q = deque([])
count: int = 0
size_list: list = []

def bfs(x, y):
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m and food_map[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
            visited[next_x][next_y] = 1
            q.append([next_x, next_y])

for _ in range(k):
    food_x, food_y = map(int, sys.stdin.readline().strip().split())
    food_map[food_x-1][food_y-1] = 1

for i in range(n):
    for j in range(m):
        if food_map[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            q.append([i, j])
            while q:
                qx, qy = q.popleft()
                count += 1
                bfs(qx, qy)
            size_list.append(count)
            count = 0

size_list.sort(reverse=True)
print(size_list[0])