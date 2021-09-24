import sys

N: int = int(sys.stdin.readline().strip())
first_prime_list: list = [2, 3, 5, 7]

def DFS(start_num: int, length: int) -> None:
    if N == 1:
        print(f'{start_num}')
        return

    p = int(start_num ** 0.5)
    for i in range(2, p + 1):
        if start_num % i == 0:
            return
            
    if start_num // ( 10 ** (N - 1)) != 0:
        print(f'{start_num}')
        return

    for j in [1, 3, 7, 9]:
        DFS(start_num * 10 + j, N)
    
    return
for i in first_prime_list:
    DFS(i, N)