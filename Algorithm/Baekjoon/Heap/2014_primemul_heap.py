import sys
import heapq
from collections import defaultdict

# k, n 받기
k, n = map(int, sys.stdin.readline().strip().split())

# 소수 리스트
prime_list: list = list(map(int, sys.stdin.readline().strip().split()))
prime_list.sort()

# 소수를 min heap에 집어 넣기
prime_queue: heapq = prime_list[:]
heapq.heapify(prime_queue)

# 최대값
max_num: int = 2 ** 31

# 이미 들어간 값인지 체크하기 위한 dict
prime_dict: defaultdict = defaultdict(int)
count: int = 0
next_num: int = 0

while True:
    next_num = heapq.heappop(prime_queue)
    count += 1

    if count == n:
        break

    for i in prime_list:
        if next_num * i < max_num and prime_dict[next_num * i] == 0:
            prime_dict[next_num * i] = 1
            heapq.heappush(prime_queue, next_num * i)

        if next_num % i == 0:
            break

print(next_num)