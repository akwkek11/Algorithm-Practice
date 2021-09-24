res = [[0 for col in range(3)] for row in range(1001)]
save = [0 for col in range(1001)]

n = int(input())
for i in range(n):
    save[i+1] = list(map(int, input().split()))

answer: int = float('inf')
for i in range(3):
    for j in range(3):
        if i == j:
            res[1][j] = save[1][j]
        else:
            res[1][j] = float('inf')

    for j in range(1, n):
        res[j + 1][0] = min(res[j][1], res[j][2]) + save[j + 1][0]
        res[j + 1][1] = min(res[j][0], res[j][2]) + save[j + 1][1]
        res[j + 1][2] = min(res[j][0], res[j][1]) + save[j + 1][2]

    for j in range(3):
        if i == j:
            continue
        else:
            answer = min(answer, res[n][j])

print(answer)