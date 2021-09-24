def solution(num_list: list) -> list:
    sorted_list: list = sorted(num_list, key=lambda x : x[0])
    
    res_list: list = []
    if len(sorted_list) >= 1:
        print('aa')
        res_list.append(sorted_list.pop())
        while sorted_list:
            start, end = sorted_list.pop()
            if res_list[-1][0] <= end:
                res_list[-1][0] = start
            else:
                res_list.append([start, end])
    
    res_list.sort(key=lambda x: x[0])
    return res_list

print(f'{solution([[1,3], [2,6], [8,10], [15,18]])}')