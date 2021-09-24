import sys

N: int = int(sys.stdin.readline().strip())
file_list: list = []

for _ in range(N):
    file_list.append(str(sys.stdin.readline().strip()))

result: list = []
for i in range(0, len(file_list[0])):
    for j in range(1, len(file_list)):
        if file_list[j][i] != file_list[0][i]:
            result.append('?')
            break

    if len(result) == i:
        result.append(file_list[0][i])

print(''.join(result))