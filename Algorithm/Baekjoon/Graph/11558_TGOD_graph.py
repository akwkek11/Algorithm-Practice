import sys

T: int = int(sys.stdin.readline().strip())
cycle_map: list = [0]
is_visited: list = []

for _ in range(T):
    N: int = int(sys.stdin.readline().strip())
    is_visited = [0 for _ in range(N+1)]
    result: int = 0
    index: int = 1
    if N == 1:
        pass
    else:
        for i in range(1, N+1):
            cycle_map.append(int(sys.stdin.readline().strip()))
        
        while True:
            if is_visited[index] == 1:
                result = 0
                break
            else:
                is_visited[index] = 1
                if index == N:
                    break
                result += 1
                index = cycle_map[index]
    
    while cycle_map:
        cycle_map.pop()
    
    cycle_map.append(0)
    print(f'{result}')