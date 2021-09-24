import sys

n, m= map(int, input().split())
arr = [0] * n
chk = [0] * (n+1)

def depth(cnt):
    if cnt == m:
        for i in range(m):
            print(arr[i], end=" ")
        print("")

    else:
        for i in range(1, n+1):
            if cnt == 0 or arr[cnt-1] <= i:
                arr[cnt] = i
                depth(cnt+1)

depth(0)
