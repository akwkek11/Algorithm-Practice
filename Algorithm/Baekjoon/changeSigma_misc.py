n, k = map(int, input().split())

l = list(map(int, input().split(',')))
m = n
for i in range(0,k):
    for j in range(0,m-1):
        l[j] = l[j+1]-l[j]
    m = m-1

res = l[:n-k]
for k in range(0, len(res)):
    if k == len(res)-1:
        print(res[k])
    else:
        print(res[k],end=',')