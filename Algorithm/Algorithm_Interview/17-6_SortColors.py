import copy

def three_way_partition(A: list, mid: int) -> list:
    res_list: list = copy.deepcopy(A)
    i: int = 0
    j: int = 0
    k: int = len(res_list)

    while j < k:
        if res_list[i] < mid:
            res_list[i], res_list[j] = res_list[j], res_list[i]
            i += 1
            j += 1
        elif res_list[j] > mid:
            k -= 1
            res_list[j], res_list[k] = res_list[k], res_list[j]
        else:
            j += 1
    
    return res_list

print(f'{three_way_partition([2,0,2,1,1,0], 1)}')