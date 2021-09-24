from collections import defaultdict

import copy
import sys

R, C, M = map(int, sys.stdin.readline().strip().split())
fish_map: list = [[0 for _ in range(C)] for _ in range(R)]
shark_dict: defaultdict = defaultdict(list)

shark_num: int = 1

'''
    dict[0] : 상어의 속력
        - 1초에 dict[0]만큼 이동한다.
    dict[1] : 상어의 이동 방향
        - 1 : 위
        - 2 : 아래
        - 3 : 오른쪽
        - 4 : 왼쪽
    dict[2] : 상어의 크기
        - 겹치면 더 큰 상어가 작은 상어를 잡아먹음
'''

for _ in range(M):
    x, y, *info = map(int, sys.stdin.readline().strip().split())
    shark_dict[shark_num] = info
    fish_map[x - 1][y - 1] = shark_num
    shark_num += 1

start: int = -1
size_sum: int = 0
temp_stack: list = []
'''
print('--------------------------')
for i in range(R):
    for j in range(C):
        print(fish_map[i][j], end = ' ') if j != C - 1 else print(fish_map[i][j])
print('--------------------------')
'''
while start != C - 1:
    # 1. 낚시왕이 1칸 이동!
    start += 1

    # 2. 가장 가까운 상어 잡기
    for i in range(R):
        if fish_map[i][start] != 0:
            size_sum += shark_dict[fish_map[i][start]][2]
            fish_map[i][start] = 0
            break
    
    # 3. 상어의 이동
    for i in range(R):
        for j in range(C):
            if fish_map[i][j] != 0:
                velocity, direction, size = shark_dict[fish_map[i][j]]
                if direction in [1, 2]:
                    if velocity > 2 * (R - 1):
                        velocity %= 2 * (R - 1)

                    now_x_position = i
                    if direction == 1:
                        if now_x_position - velocity < 0:
                            velocity -= now_x_position
                            shark_dict[fish_map[i][j]][1] = 2

                            if velocity > R - 1:
                                velocity -= R - 1
                                shark_dict[fish_map[i][j]][1] = 1
                                now_x_position = R - 1 - velocity
                            else:
                                now_x_position = velocity
                        else:
                            now_x_position -= velocity
                    
                    elif direction == 2:
                        if now_x_position + velocity >= R:
                            velocity -= R - 1 - now_x_position
                            shark_dict[fish_map[i][j]][1] = 1

                            if velocity > R - 1:
                                velocity -= R - 1
                                shark_dict[fish_map[i][j]][1] = 2
                                now_x_position = velocity
                            else:
                                now_x_position = R - 1 - velocity
                        else:
                            now_x_position += velocity
                    
                    temp_stack.append((fish_map[i][j], now_x_position, j))

                if direction in [3, 4]:
                    if velocity > 2 * (C - 1):
                        velocity %= 2 * (C - 1)

                    now_y_position = j
                    if direction == 3:
                        if now_y_position + velocity >= C:
                            velocity -= C - 1 - now_y_position
                            shark_dict[fish_map[i][j]][1] = 4

                            if velocity > C - 1:
                                velocity -= C - 1
                                shark_dict[fish_map[i][j]][1] = 3
                                now_y_position = velocity
                            else:
                                now_y_position = C - 1 - velocity
                        else:
                            now_y_position += velocity
                    
                    elif direction == 4:
                        if now_y_position - velocity < 0:
                            velocity -= now_y_position
                            shark_dict[fish_map[i][j]][1] = 3

                            if velocity > C - 1:
                                velocity -= C - 1
                                shark_dict[fish_map[i][j]][1] = 4
                                now_y_position = C - 1 - velocity
                            else:
                                now_y_position = velocity
                        else:
                            now_y_position -= velocity

                    temp_stack.append((fish_map[i][j], i, now_y_position))

                fish_map[i][j] = 0
                
    while temp_stack:
        shark_num, target_x, target_y = temp_stack.pop()
        if fish_map[target_x][target_y] == 0:
            fish_map[target_x][target_y] = shark_num
        else:
            if shark_dict[shark_num][2] > shark_dict[fish_map[target_x][target_y]][2]:
                fish_map[target_x][target_y] = shark_num
    '''
    for i in range(R):
        for j in range(C):
            print(fish_map[i][j], end = ' ') if j != C - 1 else print(fish_map[i][j])
    print('--------------------------')
    '''

print(f'{size_sum}')