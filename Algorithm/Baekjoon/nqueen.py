n = int(input())

pan = [0 for _ in range(n)]
cnt = 0

def posschk(depth):
    for i in range(depth):
        if pan[i] == pan[depth] or abs(pan[i] - pan[depth]) == abs (i-depth): return False
    return True

def nqueen(depth):
    global cnt
    if depth == n-1:
        cnt += 1
    else :
        for i in range(n):
            pan[depth+1] = i
            if posschk(depth+1):
                nqueen(depth+1)
            else :
                pan[depth+1] = 0
    pan[depth] = 0

for i in range(int(n/2)):
    pan[0] = i
    nqueen(0)

cnt *= 2

if n % 2 == 1:
    pan[0] = int(n/2)
    nqueen(0)

print(cnt)
cnt = 0