def dfs(i, j, k):
    if i > 0:
        if int(arr[i-1][j]) == 1:
            if ans[i][j] >= k or ans[i][j] == 0:
                ans[i][j] = k
                dfs(i-1, j, k+1)
    if j < b-1:
        if int(arr[i][j+1]) == 1:
            if ans[i][j] >= k or ans[i][j] == 0:
                ans[i][j] = k
                dfs(i, j+1, k+1)
    if i < a-1:
        if int(arr[i+1][j]) == 1:
            if ans[i][j] >= k or ans[i][j] == 0:
                ans[i][j] = k
                dfs(i+1, j, k+1)
    if j > 0:
        if int(arr[i][j-1]) == 1:
            if ans[i][j] >= k or ans[i][j] == 0:
                ans[i][j] = k
                dfs(i, j-1, k+1)
                
def bfs():
    q=[]
    q.append([0,0])
    ans[0][0]= 1
    while q:
        cur= q.pop(0)
        x= cur[0]
        y= cur[1]
        if cur== [a-1, b-1]:
            print(ans[x][y])
            break
        now= ans[x][y]
        for i in range(4):
            wx= x + dir[i][0]
            wy= y + dir[i][1]
            if wx >= a or wy >= b or wx < 0 or wy < 0:
                continue
            if ans[wx][wy]== 0 and int(arr[wx][wy])== 1:
                ans[wx][wy]= now+1
                q.append([wx, wy])
            
a, b = input().split()
a = int(a)
b = int(b)

arr = [0 for row in range(a)]
ans = [[0 for col in range(b)] for row in range(a)]
dir = [[0,1], [1,0], [0,-1], [-1,0]]

for i in range(a):
    arr[i] = list(input())

c = int(input())
if c == 1 :
    bfs()
elif c == 2 :
    dfs(0,0,1)
    print(ans[a-1][b-1])

'''
    Input 예시
    1 - BFS
    2 - DFS

    5 5
    10111
    10101
    10111
    11101
    00001
    1
    
    = 11
'''