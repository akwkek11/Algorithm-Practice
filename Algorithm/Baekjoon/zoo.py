a = int(input())

a1 = 3
a2 = 7

res = 0
if a==1:
    res = a1
elif a==2:
    res = a2
else:
    while (a-2)>0:
        res = 2*a2 + a1
        a1 = a2
        a2 = res
        a = a-1

print(res%9901)