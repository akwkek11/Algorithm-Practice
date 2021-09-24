import sys

N: int = int(sys.stdin.readline().strip())
num_list: list = list(map(int, sys.stdin.readline().strip().split()))
sub_list: list = [num_list[i + 1] - num_list[i] for i in range(N - 1)]

if N == 1:
    print('A')
elif N == 2:
    if num_list[0] == num_list[1]:
        print(num_list[0])
    else:
        print('A')
else:
    if sub_list[0] == 0:
        a = 0
    else:  
        a: int = sub_list[1] // sub_list[0]
    b: int = num_list[1] - num_list[0] * a

    is_calculated: bool = True
    for i in range(1, N - 1):
        if a * num_list[i] + b != num_list[i + 1]:
            is_calculated = False
            break
    
    print(f'{a * num_list[-1] + b}') if is_calculated else print('B')