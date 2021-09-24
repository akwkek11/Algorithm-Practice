'''
        1
    2   3   4
        5
        6
1-5
2-4
3-6
'''
def swap(a, b):
    tmp = dice[a]
    dice[a] = dice[b]
    dice[b] = tmp

dice = [int(0)]*7
head = 3
bottom = 6

n, m, x, y, k = map(int, input().split())

# not use m
board = [[int(k) for k in input().split()]for l in range(n)]
inst = list(map(int, input().split()))

for i in inst:
    if i == 1:
        y = y+1
    elif i == 2:
        y = y-1
    elif i == 3 :
        x = x-1
    elif i == 4 :
        x = x+1
    if x < 0 or y < 0 or x >= n or y >= m:
        if i == 1:
            y = y-1
        elif i == 2:
            y = y+1
        elif i == 3 :
            x = x+1
        elif i == 4 :
            x = x-1
    else:
        if i == 1:
            swap(2, 6)
            swap(4, 6)
            swap(3, 4)
        elif i == 2:
            swap(4, 6)
            swap(2, 6)
            swap(2, 3)
        elif i == 3:
            swap(5, 6)
            swap(1, 6)
            swap(1, 3)
        elif i == 4:
            swap(1, 6)
            swap(5, 6)
            swap(3, 5)

        if board[x][y] == 0:
            board[x][y] = dice[6]
        else:
            dice[6] = board[x][y]
            board[x][y] = 0
        print(dice[3])