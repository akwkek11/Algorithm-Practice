res = 0
n = int(input())
target = ['' for _ in range(n)]

for i in range(n):
    target[i] = list(map(int, input().split()))

b = [0 for _ in range(n)]
target.sort(key=lambda x:x[0])

for i in range(n):
    b[i] = 1
    for j in range(i):
        if target[i][1] > target[j][1] :
            if b[i] < b[j] + 1 :
                b[i] = b[j] + 1

for i in b:
    if i >= res :
        res = i

print(n-res)