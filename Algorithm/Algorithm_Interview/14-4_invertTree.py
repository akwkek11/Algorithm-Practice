import sys

num_list: list = list(map(str, sys.stdin.readline().strip().split()))

length: int = 0
while True:
    count = 2 ** length
    if len(num_list) <= 2 ** length:
        break
    else:
        length += 1

final_length = 2 ** length
for _ in range(len(num_list), final_length - 1):
    num_list.append('null')

temp: str = ''
for i in range(1, length):
    end_index = (2 ** i - 1) * 3
    for j in range(2 ** i - 1, 2 ** i - 1 + i):
        temp = num_list[j]
        num_list[j] = num_list[end_index - j]
        num_list[end_index - j] = temp

print(num_list)