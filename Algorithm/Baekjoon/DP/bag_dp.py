N, W = map(int, input().split())

l = []

bag = [0 for _ in range(W+1)]

for i in range(N):
    w, C = map(int, input().split())
    l.append((w, C))

for i in range(N):
    for j in range(W, 1, -1):
        if l[i][0] <= j:
            bag[j] = max(bag[j], bag[j-l[i][0]] + l[i][1])

print(bag[W])