from collections import deque

import sys
sys.setrecursionlimit(10 ** 5)

N: int = int(sys.stdin.readline().strip())
snake_map: list = [[0 for _ in range(N)] for _ in range(N)]

# apple = 1
# snake = 2
snake_map[0][0] = 2
snake_queue: deque = deque()
snake_queue.append((0, 0))
'''
    right = 1
    down = 2
    left = 3
    up = 4
'''
time_count: int = 0
direction_list: list = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
def simulation(x: int, y: int, direct: int) -> None:
    global time_count
    time_count += 1

    next_x: int = x + direction_list[direct][0]
    next_y: int = y + direction_list[direct][1]

    if next_x >= N or next_y >= N or next_x < 0 or next_y < 0 or snake_map[next_x][next_y] == 2:
        return

    snake_queue.append((next_x, next_y))
    if snake_map[next_x][next_y] == 0:
        delete_x, delete_y = snake_queue.popleft()
        snake_map[delete_x][delete_y] = 0
    
    snake_map[next_x][next_y] = 2

    new_direction: int = direct

    if direction_queue:
        if time_count == direction_queue[0][0]:
            now_time, change_direction = direction_queue.popleft()
            if change_direction == 'L':
                new_direction = new_direction - 1 if new_direction > 1 else 4
            elif change_direction == 'D':
                new_direction = new_direction + 1 if new_direction < 4 else 1
    '''
    for i in range(N):
        for j in range(N):
            print(f'{snake_map[i][j]}', end = ' ')
        print()
    print()
    '''
    simulation(next_x, next_y, new_direction)

# 사과 저장
apple: int = int(sys.stdin.readline().strip())
for _ in range(apple):
    x, y = map(int, sys.stdin.readline().strip().split())
    snake_map[x - 1][y - 1] = 1

# 방향 큐
direction_queue: deque = deque(())
direction_count: int = int(sys.stdin.readline().strip())
for _ in range(direction_count):
    time, direction = map(str, sys.stdin.readline().strip().split())
    direction_queue.append((int(time), direction))

simulation(0, 0, 1)
print(f'{time_count}')