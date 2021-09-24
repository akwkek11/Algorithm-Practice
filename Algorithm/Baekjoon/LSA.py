res = 0
tmp = int(input())
a = list(map(int, input().split()))
b = [0] * len(a)

for i in range(len(a)):
    for j in range(i):
        if a[i] > a[j] and b[i] < b[j] : b[i] = b[j]
    b[i] = b[i] + a[i]

for i in b:
    if i >= res : res = i

print(res)