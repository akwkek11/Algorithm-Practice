import sys
S: int = int(sys.stdin.readline().strip())
emoticon_map: list = [1000 for _ in range(1003)]
first_num: int = 0

emoticon_map[0] = 1
emoticon_map[1] = 0
for i in range(2, 6):
    emoticon_map[i] = i
emoticon_map[6] = 5

for i in range(7, 1001, 2):
    for j in range(2, (i+1)//2+1):
        if (i+1)%j == 0:
            emoticon_map[i+1] = min(emoticon_map[i+1], emoticon_map[j] + (i+1)//j)
            emoticon_map[i] = min(emoticon_map[i], emoticon_map[j] + (i+1)//j + 1)
    
    for j in range(2, i+1):
        if i%j == 0:
            first_num = j
            break

    for j in range(3, (i//first_num)+1):
        if i%j == 0:
            emoticon_map[i] = min(emoticon_map[i], emoticon_map[j] + i//j)

    for j in range(0, -3, -1):
        emoticon_map[i+j] = min(emoticon_map[i+j], emoticon_map[i+j+1] + 1, emoticon_map[i+j+2] + 2)

print(emoticon_map[S])

'''
# Solve - BFS

import sys
from collections import deque

s = int(sys.stdin.readline())
ans = [[-1] * (s + 1) for i in range(s + 1)]
ans[1][0] = 0

q = deque([(1, 0)])

while q:
    x, y = q.popleft()

    if ans[x][x] == -1:
        ans[x][x] = ans[x][y] + 1
        q.append((x, x))

    if x + y <= s and ans[x + y][y] == -1:
        ans[x + y][y] = ans[x][y] + 1
        q.append((x + y, y))

    if x - 1 >= 0 and ans[x - 1][y] == -1:
        ans[x - 1][y] = ans[x][y] + 1
        q.append((x - 1, y))

ret = float('INF')
for item in ans[s]:
    if item != -1 and ret > item:
        ret = item
print(ret)
'''