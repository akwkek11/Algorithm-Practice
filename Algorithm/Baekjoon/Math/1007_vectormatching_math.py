import itertools
import sys

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    dot_list: list = []
    N: int = int(sys.stdin.readline().strip())
    for _ in range(N):
        dot_list.append(tuple(map(int, sys.stdin.readline().strip().split())))
    plus_list: list = list(itertools.combinations([i for i in range(N)], N // 2))
    minimum_size: float = float('inf')
    for i in plus_list:
        vector_size_x: int = 0
        vector_size_y: int = 0
        for j in range(N):
            if j in i:
                vector_size_x += dot_list[j][0]
                vector_size_y += dot_list[j][1]
            else:
                vector_size_x -= dot_list[j][0]
                vector_size_y -= dot_list[j][1]
        result: float = (vector_size_x ** 2 + vector_size_y ** 2) ** 0.5
        if result < minimum_size:
            minimum_size = result
    print(minimum_size)            