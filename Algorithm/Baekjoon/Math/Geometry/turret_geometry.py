import math

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    circle_distance = math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

    if r1 == r2 and circle_distance == 0:
        print("-1")
    else:
        if r1 + r2 > circle_distance:
            if circle_distance + min(r1, r2) < max(r1, r2):
                print("0")
            elif circle_distance + min(r1, r2) == max(r1, r2):
                print("1")
            else:
                print("2")
        elif r1 + r2 == circle_distance:
            print("1")
        else:
            print("0")