import sys
from collections import deque

sys.setrecursionlimit(10**4)

n: int = int(input())
check: list = [0 for i in range(1001)]
end: int = 0
res: int = 0

def search(input_list: deque, next_node: int, is_first: bool)-> None:
    global res
    if check[next_node]:
        if is_first:
            pass
        else:
            res += 1
    else:
        check[next_node] = 1
        search(input_list, input_list[next_node], False)

for _ in range(n):
    end = int(sys.stdin.readline().strip())
    input_list = deque(map(int, sys.stdin.readline().strip().split()))
    input_list.appendleft(0)
    for i in range(1, end + 1):
        search(input_list, i, True)

    for i in range(len(check)):
        check[i] = 0

    print(res)
    res = 0
    