a, b = map(int, input().split())
c = list(map(int, input().split()))
res = 10000000

for i in range(0, a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            # print(str(c[i])+', '+str(c[j])+', '+str(c[k]))
            tmp = c[i] + c[j] + c[k]
            if (abs(tmp - b) <= abs(res - b)) and tmp - b <= 0:
                res = tmp

print(str(res))