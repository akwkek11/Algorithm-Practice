m = []
a = 1
b = 2
c = 4
d = 0

m.append(1)
m.append(2)
m.append(4)
for i in range(0, 8):
    d = a+b+c
    a = b
    b = c
    c = d
    m.append(d)

t = int(input())
cnt = 0
for cnt in range(0, t):
    n = int(input())
    n = n-1
    print(m[n])