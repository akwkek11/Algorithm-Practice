import sys

a: str = str(sys.stdin.readline().strip())
b: str = str(sys.stdin.readline().strip())

n = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            n[i][j] = n[i-1][j-1]+1
        else:
            n[i][j] = max(n[i-1][j], n[i][j-1])

max_len: int = n[len(a)][len(b)]
res_list: list = []

print(max_len)
if max_len > 0:
    target_a: int = len(a)
    target_b: int = len(b)

    while n[target_a][target_b] != 0:
        if n[target_a][target_b] == n[target_a][target_b - 1]:
            target_b -= 1
        
        elif n[target_a][target_b] == n[target_a - 1][target_b]:
            target_a -= 1
        
        else:
            res_list.append(a[target_a - 1])
            target_a -= 1
            target_b -= 1

    print(''.join(res_list[::-1]))