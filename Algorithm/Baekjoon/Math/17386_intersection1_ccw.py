import sys

# CCW
def ccw(p1: tuple, p2: tuple, p3: tuple) -> int:
    op: int = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    op -= p1[0] * p3[1] + p2[0] * p1[1] + p3[0] * p2[1]

    if op > 0:
        return 1
    
    elif op == 0:
        return 0

    else:
        return -1
def check_intersection(p1: tuple, p2: tuple, p3: tuple, p4: tuple) -> bool:

    ab: int = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    cd: int = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    is_intersect: bool = False
    if ab == 0 and cd == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        
        if p1 <= p4 and p3 <= p2:
            is_intersect = True

    elif ab <= 0 and cd <= 0:
        is_intersect = True

    return is_intersect
def meet(p1: tuple, p2: tuple, p3: tuple, p4: tuple) -> tuple:
    if p1 > p2:
        p1, p2 = p2, p1
    if p3 > p4:
        p3, p4 = p4, p3
        
    if (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]) == 0:
        if p2 == p3:
            return (int(p2[0]), int(p2[1]))
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

result: bool = check_intersection(point_1, point_2, point_3, point_4)
print('1') if result else print('0')