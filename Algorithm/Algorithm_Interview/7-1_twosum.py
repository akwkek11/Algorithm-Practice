import sys

numbers: list = list(map(int, sys.stdin.readline().strip().split()))
target: int = int(sys.stdin.readline().strip())

num_dict: dict = {}

for index, i in enumerate(numbers):
    num_dict[i] = index

for key, value in num_dict.items():
    temp_target = target - int(key)
    if temp_target >= 0 and temp_target in num_dict and value != num_dict[temp_target]:
        print(f'[{value}, {num_dict[temp_target]}]')