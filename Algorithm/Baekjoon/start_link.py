import sys

n = int(sys.stdin.readline().strip())
point = [list(map(int, sys.stdin.readline())) for _ in range(n)]

a = [0] * (n/2)
b = [0] * (n/2)

#init
for i in range(1,n+1):
    if i <= n/2 :
        a[i-1] = i
    else :
        b[i-1] = i
