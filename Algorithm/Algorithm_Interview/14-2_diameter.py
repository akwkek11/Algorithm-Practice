import sys

tree_map: list = list(map(str, sys.stdin.readline().strip().split()))

total_depth: int = len(tree_map)
left_count: int = 0
right_count: int = 0
count2: int = 0

while True:
    check: int = 2 ** left_count
    if total_depth < check:
        check_count: int = 0
        while True:
            right_check: int = 2 ** check_count + 2 ** (check_count + 1)
            if total_depth < right_check:
                check_count -= 1
                right_check = 2 ** check_count + 2 ** (check_count + 1)
                total_depth -= min(total_depth - right_check, 2 ** (check_count + 2))
                break
            check_count += 1
        break
    left_count += 1

while True:
    check: int = 2 ** right_count
    if total_depth < check:
        print(f'{max(0, left_count + right_count - 2)}')
        break
    right_count += 1