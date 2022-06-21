from collections import defaultdict
import sys

# Sieve of Eratos
def prime_list(m: int, n: int, mode: int) -> list:
    sieve: list = [True for _ in range(n + 1)] 

    p: int = int(n ** 0.5)
    for i in range(2, p + 1):
        if sieve[i] == True:          
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    # mode == 0 : return T/F Table in range
    if mode == 0:
        return sieve
    # mode == 1 : return var list in range
    elif mode == 1:
        if m == 1 : m = 2
        return [i for i in range(m, n + 1) if sieve[i] == True]

def Bipartite_matching(start: int) -> int:
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in matching_map[start]:
        if i not in is_used:
            if d[i] == 0 or Bipartite_matching(d[i]):
                d[i] = start
                is_used.append(i)
                return 1
    return 0

prime_check: list = prime_list(0, 2000, 0)
n: int = int(sys.stdin.readline().strip())
matching_map: defaultdict = defaultdict(list)
number_list: list = list(map(int, sys.stdin.readline().strip().split()))

first_number: int = number_list[0]
# key 넣어주기
for i in number_list:
    if i % 2 == 1:
        matching_map[i]

# 매칭 가능한 케이스 리스트에 넣어주기
for i in number_list:
    for j in matching_map.keys():
        if i != j and prime_check[i + j] == True:
            matching_map[j].append(i)

is_find: bool = False
while matching_map[first_number]:
    now_target: int = matching_map[first_number][0]
    d: list = [0 for _ in range(2001)]
    is_used: list = []
    for i in number_list:
        visit = [0 for _ in range(2001)]
        Bipartite_matching(i)
    if len(d) - d.count(0) == len(number_list) // 2:
        is_find = True
        print(d.index(first_number), end=' ')
    matching_map[first_number].remove(now_target)

if not is_find:
    print(-1)