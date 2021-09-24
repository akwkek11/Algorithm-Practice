import sys

tree_map: list = list(map(str, sys.stdin.readline().strip().split()))

count: int = 0
while True:
    check: int = 2 ** count
    if len(tree_map) < check:
        print(f'{count}')
        break
    count += 1