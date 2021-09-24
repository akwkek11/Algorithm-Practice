import sys

fibonacci_map: list = [0, 1, 1]

def create_map(target: int) -> int:
    global fibonacci_map
    while fibonacci_map[len(fibonacci_map)-2] != 0 or fibonacci_map[len(fibonacci_map)-1] != 1:
        fibonacci_map.append((fibonacci_map[len(fibonacci_map)-2]%target + fibonacci_map[len(fibonacci_map)-1]%target)%target)
    return len(fibonacci_map)

P: int = int(sys.stdin.readline().strip())
for _ in range(P):
    n, size = map(int, sys.stdin.readline().strip().split())
    cycle_size = create_map(size) - 2
    print(f'{n} {cycle_size}')
    while fibonacci_map:
        fibonacci_map.pop()
    fibonacci_map = [0, 1, 1]