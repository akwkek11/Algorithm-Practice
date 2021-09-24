res = 0
k = 0

for i in range(0,4):
    a, b = map(int, input().split())
    k = k - a
    k = k + b
    if res <= k:
        res = k

print(res)