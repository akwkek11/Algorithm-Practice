import copy
import sys

R, C = map(int, sys.stdin.readline().strip().split())
depth_map: list = [[0 for _ in range(C)] for _ in range(R)]
chk_list: list = [0 for _ in range(26)]
str_map: list = [str(sys.stdin.readline().strip()) for _ in range(R)]

q: set = set()
q.add((0, 0, str_map[0][0]))

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]

# 중복을 제거하기 위해선, deque가 아닌 set을 사용하는 것이 좋다.

max_depth: int = 0
def BFS(x: int, y: int, now_sentence: str) -> None:
    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < R and 0 <= next_y < C and str_map[next_x][next_y] not in now_sentence:
            q.add((next_x, next_y, now_sentence + str_map[next_x][next_y]))

while q and max_depth < 26:
    target_x, target_y, target_sentence = q.pop()
    max_depth = max(max_depth, len(target_sentence))
    BFS(target_x, target_y, target_sentence)

print(max_depth)