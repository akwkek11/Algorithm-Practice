import sys

num_list: list = list(map(int, sys.stdin.readline().strip().split()))
res_list: list = []

num_list.sort()

for i in range(len(num_list)-2):
    left: int = i + 1
    right: int = len(num_list) - 1
    while left < right:
        temp = num_list[i] + num_list[left] + num_list[right]
        if temp == 0:
            if (num_list[i], num_list[left], num_list[right]) not in res_list:
                res_list.append((num_list[i], num_list[left], num_list[right]))
            right -= 1
        else:
            if temp > 0:
                right -= 1
            else:
                left += 1

print(f'{res_list}')