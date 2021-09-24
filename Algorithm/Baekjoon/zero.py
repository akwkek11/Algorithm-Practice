n = int(input())
i = 0
s = []
res = 0

while i < n:
    k = int(input())
    if k == 0:
        del s[len(s)-1:]
    else:
        s.append(k)
    i = i+1

for j in s:
    res = res + j

print(res)