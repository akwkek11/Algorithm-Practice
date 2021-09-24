w = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

def save(a, b, c):
    global w
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return save(20, 20, 20)
    if w[a][b][c] != 0:
        return w[a][b][c]
    if a < b and b < c:
        return save(a, b, c-1) + save(a, b-1, c-1) - save(a, b-1, c)
    else:
        return save(a-1, b, c) + save(a-1, b-1, c) + save(a-1, b, c-1) - save(a-1, b-1, c-1)

for i in range(21):
    for j in range(21):
        for k in range(21):
            w[i][j][k] = save(i, j, k)

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    print("w({0}, {1}, {2}) = {3}".format(a, b, c, save(a,b,c)))