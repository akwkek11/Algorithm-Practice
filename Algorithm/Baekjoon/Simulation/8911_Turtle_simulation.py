import sys

min_y: int = 0
max_y: int = 0
min_x: int = 0
max_x: int = 0

def simulation(x: int, y: int, direction: int, next_command: int) -> None:
    global max_x, max_y, min_x, min_y

    # direction
    # L : 1, 4, 3, 2, 1, ...
    # R : 1, 2, 3, 4, 1, ...
    # 1 -> Up, 2 -> Right, 3 -> Down, 4 -> Left
    if next_command == len(command):
        return

    if command[next_command] == 'F':
        if direction == 1:
            min_x = min(min_x, x - 1)
            simulation(x - 1, y, direction, next_command + 1)
        elif direction == 2:
            max_y = max(max_y, y + 1)
            simulation(x, y + 1, direction, next_command + 1)
        elif direction == 3:
            max_x = max(max_x, x + 1)
            simulation(x + 1, y, direction, next_command + 1)
        elif direction == 4:
            min_y = min(min_y, y - 1)
            simulation(x, y - 1, direction, next_command + 1)

    elif command[next_command] == 'B':
        if direction == 1:
            max_x = max(max_x, x + 1)
            simulation(x + 1, y, direction, next_command + 1)
        elif direction == 2:
            min_y = min(min_y, y - 1)
            simulation(x, y - 1, direction, next_command + 1)
        elif direction == 3:
            min_x = min(min_x, x - 1)
            simulation(x - 1, y, direction, next_command + 1)
        elif direction == 4:
            max_y = max(max_y, y + 1)
            simulation(x, y + 1, direction, next_command + 1)

    elif command[next_command] == 'L':
        target_direction = direction - 1 if direction > 1 else 4
        simulation(x, y, target_direction, next_command + 1)
    
    elif command[next_command] == 'R':
        target_direction = direction + 1 if direction < 4 else 1
        simulation(x, y, target_direction, next_command + 1)

    return

T: int = int(sys.stdin.readline().strip())
for _ in range(T): 
    command: str = str(sys.stdin.readline().strip())
    simulation(0, 0, 1, 0)
    print(f'{(max_x - min_x) * (max_y - min_y)}')
    max_x = max_y = min_x = min_y = 0