import sys

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    N: int = int(sys.stdin.readline().strip())
    new_map: list = []
    
    for _ in range(N):
        new_map.append(list(map(int, sys.stdin.readline().strip().split())))
    
    new_map = sorted(new_map, key = lambda item : item[0])
    result: int = 1
    start: int = new_map[0][1]

    for i in range(1, N):
        if new_map[i][1] < start:
            result += 1
            start = new_map[i][1]
            
    print(f'{result}')