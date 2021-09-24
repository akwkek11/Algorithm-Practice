import sys
top: list = []
n: int = int(sys.stdin.readline().strip())
received: list = [0 for _ in range(n)]
top_value: list = [0 for _ in range(n)]
top_index: list = []

top = list(map(int, sys.stdin.readline().strip().split()))

count: int = len(top)-1
is_first: bool = True
while len(top):
    next_value: int = top.pop()
    if is_first:
        is_first = False
    else:
        while len(top_index):
            compare_index = top_index.pop()
            if next_value >= top_value[compare_index]:
                received[compare_index] = len(top) + 1
            else:
                top_index.append(compare_index)
                break

    top_index.append(count)
    top_value[count] = next_value
    count = len(top)-1

for i in range(len(received)):
    print(f'{received[i]}', end='')
    if i != len(received)-1:
        print('', end=' ')