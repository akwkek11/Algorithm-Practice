a = input()
ch = chr(ord('a'))
res = []

for i in range(0,26):
    res.append(a.find(str(ch)))
    ch = chr(ord(ch) + 1)

for i in res:
    print(i, end=' ')
