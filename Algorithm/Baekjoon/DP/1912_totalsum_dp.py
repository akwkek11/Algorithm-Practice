import sys

N: int = int(sys.stdin.readline().strip())
num_list: list = list(map(int, sys.stdin.readline().strip().split()))
total_list: list = [0 for _ in range(len(num_list))]

check: int = max(num_list)
if check <= 0:
    print(f'{check}')
else:
    for i in range(N):
        if i == 0:
            total_list[i] = num_list[i]
        else:
            if num_list[i] < 0:
                total_list[i] = total_list[i-1] + num_list[i]
            else:
                total_list[i] = max(num_list[i], num_list[i] + total_list[i-1])
    print(f'{max(total_list)}')