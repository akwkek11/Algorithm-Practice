import sys

fibonacci_map: list = [0, 1, 1]

def create_map() -> int:
    global fibonacci_map
    while fibonacci_map[len(fibonacci_map)-2] != 0 or fibonacci_map[len(fibonacci_map)-1] != 1:
        fibonacci_map.append((fibonacci_map[len(fibonacci_map)-2]%size + fibonacci_map[len(fibonacci_map)-1]%size)%size)
    return len(fibonacci_map)

n: int = int(sys.stdin.readline().strip())
size = 1000000
cycle_size = create_map() - 2

print(f'{fibonacci_map[n%cycle_size]}')