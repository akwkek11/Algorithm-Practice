import sys

N, K = map(int, sys.stdin.readline().strip().split())
eletric_list: list = list(map(int, sys.stdin.readline().strip().split()))
now_list: list = []

count: int = 0
for i in range(len(eletric_list)):
    if eletric_list[i] in now_list:
        continue
    
    if len(now_list) < N:
        now_list.append(eletric_list[i])
        continue

    next_plug: list = []
    
    for j in range(len(now_list)):
        next_index: int = eletric_list[i:].index(now_list[j]) if now_list[j] in eletric_list[i:] else float('inf')
        next_plug.append(next_index)
        if next_index == float('inf'):
            break
    
    delete_index = next_plug.index(max(next_plug))
    del now_list[delete_index]
    now_list.append(eletric_list[i])
    count += 1

print(f'{count}')