from collections import deque

import sys
sys.setrecursionlimit(10 ** 4)

N, M = map(int, sys.stdin.readline().strip().split())
virus_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

q: deque = deque(())

max_safe: int = -float('inf')

def bfs(result_map: list, x: int, y: int) -> None:
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M and result_map[next_x][next_y] == 0:
            result_map[next_x][next_y] = 2
            q.append((next_x, next_y))

def simulation(count: int, x: int, y: int) -> None:
    global max_safe

    if count == 3:
        res_map: list = [[0 for _ in range(M)] for _ in range(N)]
        result: int = 0
        for i in range(N):
            for j in range(M):
                if virus_map[i][j] != 0:
                    res_map[i][j] = virus_map[i][j]
                
                if virus_map[i][j] == 2:
                    q.append((i, j))
        
        while q:
            target_x, target_y = q.popleft()
            bfs(res_map, target_x, target_y)

        for i in range(N):
            for j in range(M):
                if res_map[i][j] == 0:
                    result += 1
        
        max_safe = max(max_safe, result)
        return
    
    for i in range(x, N):
        for j in range(y, M):
            if virus_map[i][j] == 0:
                virus_map[i][j] = 1
                simulation(count + 1, i, j + 1)
                virus_map[i][j] = 0
        y = 0

    return

simulation(0, 0, 0)
print(f'{max_safe}')