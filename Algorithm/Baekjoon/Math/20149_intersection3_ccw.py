import sys

def ccw(p1: tuple, p2: tuple, p3: tuple) -> int:
    op: int = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    op -= p1[0] * p3[1] + p2[0] * p1[1] + p3[0] * p2[1]

    if op > 0:
        return 1
    
    elif op == 0:
        return 0

    else:
        return -1

def meet(p1: tuple, p2: tuple, p3: tuple, p4: tuple) -> tuple:
    if (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]) == 0:
        if p2 == p3:
            return (int(p2[0]), int(p2[1]))
        elif p1 == p4:
            return (int(p1[0]), int(p1[1]))
        else:
            return (-float('inf'), -float('inf'))
    
    else:
        point_x: float = ((p1[0] * p2[1] - p1[1] * p2[0]) * (p3[0] - p4[0]) - (p1[0] - p2[0]) * (p3[0] * p4[1] - p3[1] * p4[0])) / ((p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]))
        point_y: float = ((p1[0] * p2[1] - p1[1] * p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] * p4[1] - p3[1] * p4[0])) / ((p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]))
        return (point_x, point_y)

x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
point_1: tuple = (x1, y1)
point_2: tuple = (x2, y2)

x3, y3, x4, y4 = map(int, sys.stdin.readline().strip().split())
point_3: tuple = (x3, y3)
point_4: tuple = (x4, y4)

ab: int = ccw(point_1, point_2, point_3) * ccw(point_1, point_2, point_4)
cd: int = ccw(point_3, point_4, point_1) * ccw(point_3, point_4, point_2)

is_intersect: bool = False
if ab == 0 and cd == 0:
    if point_1 > point_2:
        point_1, point_2 = point_2, point_1
    if point_3 > point_4:
        point_3, point_4 = point_4, point_3
    
    if point_1 <= point_4 and point_3 <= point_2:
        is_intersect = True

elif ab <= 0 and cd <= 0:
    is_intersect = True

print('1') if is_intersect else print('0')
if is_intersect:
    meet_point: tuple = meet(point_1, point_2, point_3, point_4)
    if meet_point[0] != -float('inf'):
        print(f'{meet_point[0]} {meet_point[1]}')