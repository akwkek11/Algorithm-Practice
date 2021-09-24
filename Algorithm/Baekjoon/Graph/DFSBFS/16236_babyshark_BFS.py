from collections import deque

import sys

def bfs(x: int, y: int, step: int) -> None:
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < N and 0 <= next_y < N and is_visited[next_x][next_y] == 0 and fish_map[next_x][next_y] <= shark_size:
            is_visited[next_x][next_y] = 1
            q.append((next_x, next_y, step + 1))

# 사이즈
N: int = int(sys.stdin.readline().strip())

# 아기상어 크기
shark_size: int = 2

# 물고기 먹은 횟수
eat_count: int = 0

# 걸어간 길이
total_time: int = 0

# up, left, right, down
dx: list = [-1, 0, 0, 1] 
dy: list = [0, -1, 1, 0]

# 물고기 맵
fish_map: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 걸어온 길 중복체크 리스트
is_visited: list = [[0 for _ in range(N)] for _ in range(N)]

# x, y, step
q: deque = deque(())

# 여기에 원래 아기상어 좌표 저장
save_stack: list = []

# 후보군 저장
candidates: list = []

# 첫 아기상어를 찾아 나서는 코드
for i in range(len(fish_map)):
    for j in range(len(fish_map)):
        if fish_map[i][j] == 9:
            is_visited[i][j] = 1
            q.append((i, j, 0))
            save_stack.append((i, j))
            break
while q:
    target_x, target_y, target_count = q.popleft()
    if 0 < fish_map[target_x][target_y] < shark_size:
        # 후보군 등록
        candidates.append((target_x, target_y))

        # step 저장
        final_count: int = target_count

        # 다른 후보군도 탐색
        while q:
            candidates_x, candidates_y, candidates_count = q.popleft()
            if target_count == candidates_count and 0 < fish_map[candidates_x][candidates_y] < shark_size:
                candidates.append((candidates_x, candidates_y))

        # 조건에 맞는 x, y 좌표
        candidates.sort(key=lambda x : (x[0], x[1]), reverse = True)
        final_x, final_y = candidates.pop()
        candidates.clear()

        # 원래 좌표 가져오기
        original_x, original_y = save_stack.pop()

        # 아기상어 예전 좌표, 현재 좌표 바꿔주기
        fish_map[final_x][final_y], fish_map[original_x][original_y] = 9, 0

        # 아기상어 현재 좌표를 Deque에 넣고, stack에 저장
        q.append((final_x, final_y, 0))
        save_stack.append((final_x, final_y))

        # 먹은 마리수 늘리고, 스탭 더해주기
        eat_count += 1
        total_time += final_count

        # 만약 크기만큼 먹었다면 사이즈 늘려주기
        if eat_count == shark_size:
            shark_size += 1
            eat_count = 0

        # 디버깅용!
        '''
        for i in range(len(is_visited)):
            for j in range(len(is_visited)):
                print(f'{fish_map[i][j]}', end = ' ') if j < len(fish_map) - 1 else print(f'{fish_map[i][j]}')
        print(f'now_step : {total_time}, now_size : {shark_size}, now_count : {eat_count}', end='\n\n')
        '''

        # 방문했던 기록 초기화
        for i in range(len(is_visited)):
            for j in range(len(is_visited)):
                is_visited[i][j] = 0
    else:
        # 만약 자기보다 작지 않다면 재탐색
        bfs(target_x, target_y, target_count)

print(f'{total_time}')