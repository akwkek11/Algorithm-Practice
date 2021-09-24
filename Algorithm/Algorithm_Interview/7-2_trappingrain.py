import sys

block_list: list = list(map(int, sys.stdin.readline().strip().split()))
pop_block_list: list = []

result: int = 0

def trapping_calculate(target_list: list, pop_list: list) -> int:
    res: int = 0
    while target_list:
        next_num: int = target_list.pop()
        while pop_list:
            chk: int = pop_list.pop()

            if not pop_list:
                if next_num < chk:
                    pop_list.append(chk)
                break

            if chk <= next_num and pop_list[0] <= next_num:
                res += min(pop_list[0], next_num) - chk
            else:
                pop_list.append(chk)
                break
        pop_list.append(next_num)
    return res

result += trapping_calculate(block_list, pop_block_list)
result += trapping_calculate(pop_block_list, block_list)
print(f'{result}')
