N, L = map(int, input().split())

hole = list(map(int, input().split()))
hole.sort()

count = 0
line = 0
i = 0

while True:
    line = hole[i] - 0.5 + L
    count += 1

    if i == N-1:
        break

    else:
        while True:
            i += 1
            if i == N:
                break
            elif hole[i] > line - 0.5:
                break
        
        if i == N:
            break
print(count)