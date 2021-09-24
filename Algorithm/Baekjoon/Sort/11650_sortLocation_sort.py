import sys

N: int = int(sys.stdin.readline().strip())
location_list: list = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    location_list.append((x, y))

location_list.sort(key=lambda x : (x[0], x[1]))

for i in location_list:
    print(f'{i[0]} {i[1]}')