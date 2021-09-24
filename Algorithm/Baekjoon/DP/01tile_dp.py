a1 = 1
a2 = 2
tmp1 = 0
tmp2 = 0
div = 15746

n = int(input())
res = 2
# n == 1
if n == 1:
    res = a1
# n == 2
elif n == 2:
    res = a2
else:
    for k in range(n-2):
        # n == 3
        if k == 0:
            res = a1 + a2
        else:
            # n == 4
            if k == 1:
                tmp1 = a2
            # n > 4
            else:
                tmp1 = tmp2
            tmp2 = res
            res = (res + tmp1)%div

print(res)