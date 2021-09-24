import sys

n: int = int(sys.stdin.readline().strip())
dot_list: list = []
class_dot_list: list = [[] for _ in range(5001)]
dot_now: int = 0
start_index: int = 0

result: int = 0

for i in range(n):
    dot_list.append(list(map(int, sys.stdin.readline().strip().split())))

dot_list.sort(key=lambda x:x[0])

for i in dot_list:
    class_dot_list[i[1]].append(i[0])

for i in class_dot_list:
    if len(i) == 0 or len(i) == 1:
        pass
    elif len(i) == 2:
        result += 2*(i[1]-i[0])
    else:
        for j in range(len(i)):
            if j == 0:
                result += i[j+1]-i[j]
            elif j == len(i)-1:
                result += i[j]-i[j-1]
            else:
                result += min(i[j]-i[j-1], i[j+1]-i[j])

print(f'{result}')