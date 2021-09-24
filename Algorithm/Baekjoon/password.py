m, n= map(int, input().split())
arr = [0] * n
chk = [0] * (n+1)
alp = input().split()
alp.sort()

collection = ['a', 'e', 'i', 'o', 'u']
ccount = 0
vcount = 0

def depth(cnt):
    if cnt == m:
        global ccount, vcount
        for i in range(m):
            if alp[arr[i]] in collection:
                ccount += 1
        vcount = m-ccount
        
        if ccount >=1 and vcount >=2 :
            for i in range(m):
                print(alp[arr[i]], end="")
            print("")
        ccount = 0
        vcount = 0
    else:
        for i in range(0, n):
            if chk[i] == 0 and (cnt == 0 or arr[cnt-1] <= i):
                chk[i] = 1
                arr[cnt] = i
                depth(cnt+1)
                chk[i] = 0

depth(0)