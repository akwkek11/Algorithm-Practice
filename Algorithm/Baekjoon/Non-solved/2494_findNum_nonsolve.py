#not solved

import sys
sys.setrecursionlimit(100000)

def dp(start_index: int) -> int:
    if start_index == 0:
        last_target: int = abs(end[start_index] - start[start_index])
        return min(last_target, 10 - last_target)
    else:
        start_diff: int = start[start_index] - start[start_index - 1]
        end_diff: int = end[start_index] - end[start_index - 1]
        reverse_start_diff: int = (10 + start_diff) if start_diff < 0 else -(10 - start_diff)

        check_start_diff: int = abs(end_diff - reverse_start_diff)
        if check_start_diff > 10:
            check_start_diff = 20 - check_start_diff

        print(abs(end_diff - start_diff), check_start_diff)
        final_diff = min(abs(end_diff - start_diff), check_start_diff)
        print(final_diff)
        return final_diff + dp(start_index - 1)

N: int = int(sys.stdin.readline().strip())
start: list = list(map(int, list(str(sys.stdin.readline().strip()))))
end: list = list(map(int, list(str(sys.stdin.readline().strip()))))
save_list: list = [0 for _ in range(N)]

result: int = dp(N - 1)
print(f'{result}')

'''
import copy
import sys

sys.setrecursionlimit(1000000)

def dp(start_index: int, now_list: list) -> int:
    if start_index == len(now_list):
        return 0

    target: int = now_list[start_index]
    new_list: list = copy.deepcopy(now_list)
    cost1: int = 0
    cost2: int = 0

    if now_list == end:
        return 0
    else:
        final_number: int = end[start_index]
        if final_number < target:
            final_number += 10
        
        cost1: int = final_number - target
        for i in range(start_index + 1, len(new_list)):
            new_list[i] += cost1
            if new_list[i] >= 10:
                new_list[i] -= 10
        
        cost2: int = 10 - cost1
        now_list[start_index] = new_list[start_index] = end[start_index]
        print(cost1, cost2)
        print(new_list, now_list)
        return min(cost2 + dp(start_index + 1, now_list), cost1 + dp(start_index + 1, new_list))

N: int = int(sys.stdin.readline().strip())
start: list = list(map(int, list(str(sys.stdin.readline().strip()))))
end: list = list(map(int, list(str(sys.stdin.readline().strip()))))

result = dp(0, start)
print(f'{result}')
'''

