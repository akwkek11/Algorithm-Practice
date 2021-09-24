a, b = map(str, input().split())
c = ''.join(reversed(a))
d = ''.join(reversed(b))
if int(c) >= int(d):
    print(c)
else:
    print(d)