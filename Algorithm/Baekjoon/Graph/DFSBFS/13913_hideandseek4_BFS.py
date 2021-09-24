from collections import deque

import sys

'''
sys.setrecursionlimit(10 ** 6)

N, K = map(int, sys.stdin.readline().strip().split())
q: deque = deque()
num_map: list = [float('inf') for _ in range(100001)]
result_list: list = []
num_map[N] = 0
q.append(N)

def BFS(x: int) -> None:
    if 0 <= x - 1 and num_map[x - 1] == float('inf'):
        num_map[x - 1] = num_map[x] + 1
        q.append(x - 1)
    
    if x + 1 <= 100000 and num_map[x + 1] == float('inf'):
        num_map[x + 1] = num_map[x] + 1
        q.append(x + 1)
        
    if x * 2 <= 100000 and num_map[x * 2] == float('inf'):
        num_map[x * 2] = num_map[x] + 1
        q.append(x * 2)

def backtracking(x: int) -> bool:
    if x == N:
        result_list.append(x)
        return True

    if 0 <= x - 1 and num_map[x - 1] == num_map[x] - 1:
        if backtracking(x - 1):
            result_list.append(x)
            return True

    if x + 1 <= 100000 and num_map[x + 1] == num_map[x] - 1:
        if backtracking(x + 1):
            result_list.append(x)
            return True
    
    if x % 2 == 0 and 0 <= x // 2 and num_map[x // 2] == num_map[x] - 1:
        if backtracking(x // 2):
            result_list.append(x)
            return True
    
    return False

while q:
    target_x = q.popleft()
    if target_x == K:
        break
    BFS(target_x)

backtracking(K)
print(f'{len(result_list) - 1}')
result_list = result_list[::-1]
while result_list:
    print_num: int = result_list.pop()
    print(f'{print_num}', end = ' ') if result_list else print(f'{print_num}')
'''

# 더 빠른 코드
N, K = map(int, sys.stdin.readline().strip().split())
q: deque = deque()
num_map: list = [float('inf') for _ in range(100001)]
is_visited: list = [-1 for _ in range(100001)]
result_list: list = []
num_map[N] = 0
is_visited[N] = N
q.append(N)

def BFS(x: int) -> None:
    if 0 <= x - 1 and num_map[x - 1] == float('inf'):
        num_map[x - 1] = num_map[x] + 1
        is_visited[x - 1] = x
        q.append(x - 1)
    
    if x + 1 <= 100000 and num_map[x + 1] == float('inf'):
        num_map[x + 1] = num_map[x] + 1
        is_visited[x + 1] = x
        q.append(x + 1)
        
    if x * 2 <= 100000 and num_map[x * 2] == float('inf'):
        num_map[x * 2] = num_map[x] + 1
        is_visited[x * 2] = x
        q.append(x * 2)

while q:
    target_x = q.popleft()
    if target_x == K:
        break
    BFS(target_x)

index: int = K
while index != N and index != -1:
    result_list.append(index)
    index = is_visited[index]
result_list.append(N)

print(f'{len(result_list) - 1}')
print(*result_list[::-1])