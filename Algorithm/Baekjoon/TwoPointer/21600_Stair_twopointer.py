import sys
sys_input = sys.stdin

N: int = int(sys_input.readline().strip())
num_map: list = list(map(int, sys_input.readline().strip().split()))

start: int = 0
end: int = 0
max_length: int = -float('inf')
length: int = 1

while start < N - 1 and end < N - 1:
    if length == 1:
        if num_map[start] >= length:
            end = start
            while True:
                if end >= N - 1:
                    break

                if num_map[end + 1] >= length + 1:
                    end += 1
                    length += 1
                else:
                    start += 1
                    length -= 1
                    if start > end and length == 0:
                        length = 1
                        break

                max_length = max(max_length, length)
        else:
            start += 1
if max_length == -float('inf'):
    max_length = 1
print(f'{max_length}')