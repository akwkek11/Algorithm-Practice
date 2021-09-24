n = int(input())

cycle = [(10, 0),
         (1, 0),
         (6, 2, 4, 8),
         (1, 3, 9, 7),
         (6, 4),
         (5, 0),
         (6, 0),
         (1, 7, 9, 3),
         (6, 8, 4, 2),
         (1, 9)]

size = [1, 1, 4, 4, 2, 1, 1, 4, 4, 2]

for i in range(n):
    a, b = map(int, input().split())

    print("{0}".format(cycle[a%10][b%size[a%10]]))