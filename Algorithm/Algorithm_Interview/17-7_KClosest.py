import heapq

def solution(array: list, target: int) -> list:
    sorted_list: heapq = []
    for i in array:
        heapq.heappush(sorted_list, ((i[0] ** 2 + i[1] ** 2), [i[0], i[1]]))

    get_array: list = []
    last_num: int = -float('inf')
    for i in range(0, target):
        get_array.append(heapq.heappop(sorted_list)[1])
        last_num = max(last_num, heapq.heappop(sorted_list)[0])

    while sorted_list:
        now_num, now_array = heapq.heappop(sorted_list)
        if now_num != last_num:
            break
        get_array.append(now_array)

    return get_array

print(f'{solution([[3, 3], [5, -1], [-2, 4]], 2)}')
print(f'{solution([[1, 3], [2, -2]], 1)}')