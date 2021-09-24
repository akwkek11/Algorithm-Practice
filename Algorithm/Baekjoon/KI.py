import math

def modInverse(k1, k2):
    r = -1
    for i in range(0, k2):
        tmp = (k1*i) % k2
        if tmp == 1 :
            r = i
            break
    return r

def gcd(k1, k2):
    while(k2):
        k1, k2 = k2, k1 % k2
    return k1

def lcm(k1, k2, g1):
    return int(k1*k2/g1)
k = int(input())
res = [0]*k

a = 0
b = 0
c = 0
d = 0
for i in range(0, k):
    M, N, x, y = list(map(int, input().split()))
    if M == N == x == y :
        res[i] = x
    else:
        if x - y <= 0:
            a = M
            c = N
            d = x
        else:
            a = N
            c = M
            d = y
        b = x - y <= 0 and y - x or x - y
        g = gcd(gcd(a,c), b)
        l = lcm(a, c, gcd(a, c))

        an, n1 = divmod(a, g)
        bn, n2 = divmod(b, g)
        cn, n3 = divmod(c, g)
        p = modInverse(an, cn)
        if p == -1 :
            res[i] = -1
        else :
            print(str(l) + ', ' + str(g) + ', ' + str(p) + ', ' + str(an) + ', ' + str(bn) + ', ' + str(cn))
            res[i] = a*((bn*p) % cn) + d

for i in range(0, k):
    print(str(res[i]))