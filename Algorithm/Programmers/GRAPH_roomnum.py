from collections import defaultdict

def solution(arrows):
    x: int = 0
    y: int = 0

    check: defaultdict = defaultdict(int)
    line_history: defaultdict = defaultdict(int)
    check[(x, y)] = 1
    direction: list = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    answer: int = 0

    for next_direction in arrows:
        next_x: int = x + direction[next_direction][0]
        next_y: int = y + direction[next_direction][1]
        
        if next_direction in [1, 3, 5, 7]:
            if check[(x + direction[next_direction][0], y)] == 1 and check[(x, y + direction[next_direction][1])] == 1:
                if line_history[(x, y, next_x, next_y)] == 0 and line_history[(x + direction[next_direction][0], y, x, y + direction[next_direction][1])] == 1:
                    answer += 1
        
        if check[(next_x, next_y)] == 1 and line_history[(x, y, next_x, next_y)] == 0:
            answer += 1
        
        check[(next_x, next_y)] = 1
        line_history[(x, y, next_x, next_y)] = 1
        line_history[(next_x, next_y, x, y)] = 1

        x = next_x
        y = next_y

    return answer

print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))