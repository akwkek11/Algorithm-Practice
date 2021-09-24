t = int(input())
res = [0] * t
f = [0, 5000000, 3000000, 2000000, 500000, 300000, 100000]
s = [5120000, 2560000, 1280000, 640000, 320000]

for i in range(0, t):
    p = 0
    k = 0
    a, b = map(int, input().split())
    for j in range(1, 7):
        if a == 0:
            break
        p = p + j
        if a <= p:
            k = k + f[j]
            break
    p = 0
    for n in range(0, 5):
        if b == 0:
            break
        p = p + 2**n
        if b <= p:
            k = k + s[n]
            break
    res[i] = k

for i in range(0, t):
    print(str(res[i]))
