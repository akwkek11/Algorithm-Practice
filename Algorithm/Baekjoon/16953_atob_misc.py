import sys

a, b = map(int, sys.stdin.readline().strip().split())
count: int = 0

while True:
    if b == 0:
        count = -1
        break

    if b%2 == 0:
        if a == b:
            break
        else:
            b //= 2
            count += 1
    else:
        if a == b:
            break
        else:
            if b%10 == 1:
                b //= 10
                count += 1
            else:
                count = -1
                break

if count != -1:
    count += 1

print(count)