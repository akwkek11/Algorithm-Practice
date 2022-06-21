import sys

decrease_map: list = [[], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
map_index: list = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
for i in range(9):
    decrease_map.append([])
    map_index.append([1])

for i in range(1, 8):
    for j in range(1, 9):
        map_index[i].append(map_index[i][-1] + map_index[i - 1][j])

for i in range(2, 11):
    x_index: int = i - 2
    y_index: int = 10 - i
    
    if y_index == 0:
        decrease_map[i].append(9876543210)
        break
    
    for j in range(i - 1, 10):
        for k in range(map_index[x_index][j - i + 1]):
            decrease_map[i].append(j * (10 ** (i-1)) + decrease_map[i - 1][k])

result: list = []
for l in decrease_map:
    result.extend(l)

target: int = int(sys.stdin.readline().strip())
if target - 1 >= len(result):
    print(-1)
else:
    print(result[target - 1])