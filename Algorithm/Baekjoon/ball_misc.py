n = int(input())
cup = [0,1,2,3]

def search(a,b):
    k = 0
    l = 0
    for i in range(0,4):
        if cup[i] == a:
            k = i
        elif cup[i] == b:
            l = i
    tmp = cup[k]
    cup[k] = cup[l]
    cup[l] = tmp

for i in range(0,n):
    a,b = map(int, input().split())
    search(a,b)

print(cup[1])