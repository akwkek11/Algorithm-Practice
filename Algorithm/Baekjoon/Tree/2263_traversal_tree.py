import sys
sys.setrecursionlimit(10 ** 6)

N: int = int(sys.stdin.readline().strip())
in_order: list = list(map(int, sys.stdin.readline().strip().split()))
post_order: list = list(map(int, sys.stdin.readline().strip().split()))

in_order_position: list = [0 for _ in range(len(in_order) + 1)]

for index, value in enumerate(in_order):
    in_order_position[value] = index

pre_order: list = []
def get_pre_order(in_start: int, in_end: int, post_start: int, post_end: int) -> None:
    if post_start > post_end or in_start > in_end:
        return
    
    root: int = post_order[post_end]
    pre_order.append(str(root))

    in_order_root: int = in_order_position[root]
    next_left: int =  in_order_root - in_start

    get_pre_order(in_start, in_order_root - 1, post_start, post_start + next_left - 1)
    get_pre_order(in_order_root + 1, in_end, post_start + next_left, post_end - 1)

get_pre_order(0, N - 1, 0, N - 1)
print(" ".join(pre_order))

'''
def search(arr: list, x: int, n: int) -> int:
    for i in range(n):
        if (arr[i] == x):
            return i
    return -1

def get_post_order(n: int) -> None:
     =
    root: int = search(In, pre[0], n)
 
    # If left subtree is not empty
    if (root != 0):
        get_post_order(in_order, pre_order[1 : n], root)
 
    # If right subtree is not empty
    if (root != n - 1):
        get_post_order(in_order[root + 1 : n], pre[root + 1 : n], n - root - 1)
    
    post_order.append(pre_order[0])
'''
