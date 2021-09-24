n = int(input())
c = list(map(int, input().split()))

a = 0
b = 0
sub = 2100000000

k = 0
l = len(c) - 1

while k != l:
    tmp = abs(c[k]+c[l])
    if tmp <= sub:
        sub = tmp
        a = k
        b = l
    
    if c[k]+c[l] < 0:
        k = k+1
    else:
        l = l-1

print(str(c[a])+' '+str(c[b]))