import sys

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    n: int = int(sys.stdin.readline().strip())
    space_map: list = []
    for _ in range(n):
        space_map.append(list(map(int, sys.stdin.readline().strip().split())))

    count: int = 0
    for i in space_map:
        r1 = (((i[0] - x1) ** 2) + ((i[1] - y1) ** 2)) ** 0.5
        r2 = (((i[0] - x2) ** 2) + ((i[1] - y2) ** 2)) ** 0.5
        if (i[2] > r1 and i[2] < r2) or (i[2] < r1 and i[2] > r2):
            count += 1

    print(f'{count}')