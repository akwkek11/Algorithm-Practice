n = int(input())
a = [0]*(n+1)
r = [0]*(n+1)

for i in range(1,n+1):
    a[i] = int(input())

r[1] = a[1]

if n == 1 :
    print(r[n])
else:
    r[2] = a[1] + a[2]
    if n == 2 :
        print(r[n])
    else:
        for i in range(3, n+1):
            r[i] = max(r[i-2]+a[i], r[i-3]+a[i-1]+a[i], r[i-1])
        print(r[n])