a = input()
b = input()

n = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            n[i][j] = n[i-1][j-1]+1
        else:
            n[i][j] = max(n[i-1][j], n[i][j-1])

print(n[len(a)][len(b)])