import sys

K, N = map(int, sys.stdin.readline().strip().split())
numbers: list = [int(sys.stdin.readline().strip()) for _ in range(K)]
size = len(str(max(numbers))) + 1

numbers = list(map(str, numbers))
numbers.sort(key=lambda x: x*size, reverse=True)
index: int = 0
max_index: list = [0, 0]
for i, value in enumerate(numbers):
    if max_index[1] < len(value):
        max_index[0] = i
        max_index[1] = len(value)

count: int = 0
res_str: list = []
while count < N:
    if index < max_index[0]:
        res_str.append(numbers[index])
        index += 1
    elif N - count > len(numbers) - index:
        res_str.append(numbers[index])
    else:
        res_str.append(numbers[index])
        index += 1
    
    count += 1
print(''.join(res_str))