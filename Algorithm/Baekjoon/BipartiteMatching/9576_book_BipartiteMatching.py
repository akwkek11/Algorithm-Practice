from collections import defaultdict

import sys

def Bipartite_matching(start: int) -> int:
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in book_map[start]:
        if d[i] == 0 or Bipartite_matching(d[i]):
            d[i] = start
            return 1
    return 0

T: int = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())

    # 각 책을 원하는 사람이 M명이므로 book_map의 size는 m
    book_map: defaultdict = defaultdict(list)

    # 총 몇 개를 배분하냐는 n이므로 d는 1~n까지 사용
    d: list = [0 for i in range(n + 1)]

    # m명에 대한 정보 입력
    for i in range(1, m + 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        for j in range(a, b + 1):
            book_map[i].append(j)

    # m명을 매칭하는 것에 대한 탐색
    for i in range(1, m + 1):
        visit = [0 for _ in range(m + 1)]
        Bipartite_matching(i)

    print(len(d) - d.count(0))