import heapq

def solution(array: list) -> list:
    final_list: list = []
    save_list: heapq = []

    # 기본적으로 min-heap
    # max-heap처럼 써주려면 (-j, j)로 넣어서 [1]번째 요소 참조하기.
    # 가운데 값 참조는 max-heap, min-heap에 하나씩 넣으면서 대소비교, max-heap > min-heap이면 swap후 max-heap의 1번째 원소
    for i in array:
        for j in i:
            heapq.heappush(save_list, j)

    while save_list:
        final_list.append(heapq.heappop(save_list))
    
    return final_list

print(f'{solution([[1, 4, 5], [1, 3, 4], [2, 6]])}')