import sys

def tonic_count(num_list: list) -> list:
    target: list = [0 for _ in range(N)]
    for i in range(N):
        target[i] = 1
        for j in range(N):
            if num_list[i] > num_list[j]:
                if target[i] < target[j] + 1:
                    target[i] = target[j] + 1

    return target

N: int = int(sys.stdin.readline().strip())
num_map: list = list(map(int, sys.stdin.readline().strip().split()))
count: list = tonic_count(num_map)
reverse_count: list = tonic_count(num_map[::-1])
reverse_count = reverse_count[::-1]
final_count: list = []
for i in range(N):
    final_count.append(count[i] + reverse_count[i])
final_count.sort()
print(f'{final_count.pop() - 1}')

