a1 = 1
a2 = 2
a3 = 0

t = int(input())

c = 1
for i in range(0,t):
    a, b = map(int, input().split())
    l = b-a
    
    if l == 1:
        print(1)
    elif l == 2:
        print(2)
    else:
        while True:
            a3 = c+2+a1
            a1 = a2
            a2 = a3
            if l <= a3:
                print(str(c+2))
                break
            c = c+1

    a1 = 1
    a2 = 2
    a3 = 0
    c = 1