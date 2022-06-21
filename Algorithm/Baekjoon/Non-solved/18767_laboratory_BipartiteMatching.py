from collections import defaultdict

import sys
sys.setrecursionlimit(10 ** 5)

def Bipartite_matching(start: int) -> int:
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in work_map[start]:
        if d[i] == 0 or Bipartite_matching(d[i]):
            d[i] = start
            return 1
    return 0

T: int = int(sys.stdin.readline().strip())
room: list = ['', 'A', 'B', 'C']

for _ in range(T):
    n: int = int(sys.stdin.readline().strip())
    work_map: defaultdict = defaultdict(list)
    num_room: list = list(map(int, sys.stdin.readline().strip().split()))
    d: list = [0 for i in range(sum(num_room) + 1)]
    index_room: list = [0, (1, num_room[0]), (num_room[0] + 1, num_room[0] + num_room[1]), (num_room[0] + num_room[1] + 1, sum(num_room))]
    
    for i in range(1, 3 + 1):
        num, *want = map(int, sys.stdin.readline().strip().split())
        for j in want:
            for k in range(index_room[i][0], index_room[i][1] + 1):
                work_map[j].append(k)
                
    for i in range(1, n + 1):
        visit = [0 for _ in range(n + 1)]
        Bipartite_matching(i)
    
    people_room: list = [0 for _ in range(n + 1)]
    print(len(d) - d.count(0))
    for i in range(len(d)):
        if d[i] != 0:
            for j in range(1, 3 + 1):
                if index_room[j][0] <= i <= index_room[j][1]:
                    people_room[d[i]] = j
                    break
    
    for index, value in enumerate(people_room):
        room_alp: str = room[value]
        if value > 0:
            print(f'{index} {room_alp}')
            