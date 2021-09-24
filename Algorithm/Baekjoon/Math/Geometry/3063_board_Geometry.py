import sys

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().strip().split())
    target_x1, target_y1, target_x2, target_y2 = 0, 0, 0, 0
    is_out: bool = False
    if x3 <= x1:
        target_x1 = x1
    elif x2 <= x3:
        is_out = True
    else:
        target_x1 = x3

    if y3 <= y1:
        target_y1 = y1
    elif y2 <= y3:
        is_out = True
    else:
        target_y1 = y3

    if x4 >= x2:
        target_x2 = x2
    elif x1 >= x4:
        is_out = True
    else:
        target_x2 = x4

    if y4 >= y2:
        target_y2 = y2
    elif y1 >= y4:
        is_out = True
    else:
        target_y2 = y4
    subtract: int = (target_x2 - target_x1) * (target_y2 - target_y1) if not is_out else 0
    area = (x2 - x1) * (y2 - y1) - subtract
    print(f'{area}')