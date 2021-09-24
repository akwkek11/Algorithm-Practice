from itertools import combinations

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

    if ab == 0 and cd == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        
        return p1 <= p4 and p3 <= p2
    return ab <= 0 and cd <= 0
    
def meet(p1: tuple, p2: tuple, p3: tuple, p4: tuple) -> tuple:
    if p1 > p2:
        p1, p2 = p2, p1
    if p3 > p4:
        p3, p4 = p4, p3

    if (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]) == 0:
        if p2 == p3:
            return (p2[0], p2[1])
        elif p1 == p4:
            return (p1[0], p1[1])
        else:
            return (-float('inf'), -float('inf'))
    
    else:
        point_x: float = ((p1[0] * p2[1] - p1[1] * p2[0]) * (p3[0] - p4[0]) - (p1[0] - p2[0]) * (p3[0] * p4[1] - p3[1] * p4[0])) / ((p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]))
        point_y: float = ((p1[0] * p2[1] - p1[1] * p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] * p4[1] - p3[1] * p4[0])) / ((p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]))
        return (point_x, point_y)

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    rec_point: list = []
    rec_x1, rec_y1, rec_x2, rec_y2 = map(int, sys.stdin.readline().strip().split())
    rec_point.append([(rec_x1, rec_y1), (rec_x1, rec_y2)])
    rec_point.append([(rec_x1, rec_y2), (rec_x2, rec_y2)])
    rec_point.append([(rec_x2, rec_y2), (rec_x2, rec_y1)])
    rec_point.append([(rec_x2, rec_y1), (rec_x1, rec_y1)])

    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    point_1: tuple = (x1, y1)
    point_2: tuple = (x2, y2)

    intersection_point: list = []
    result: int = 0
    for i in range(len(rec_point)):
        if check_intersection(point_1, point_2, rec_point[i][0], rec_point[i][1]):
            get_intersection: tuple = meet(point_1, point_2, rec_point[i][0], rec_point[i][1])
            if get_intersection[0] == -float('inf'):
                result = 4
                break
            if get_intersection not in intersection_point:
                intersection_point.append(get_intersection)

    if result != 4:
        result = len(intersection_point)
    
    print(f'{result}')