from collections import deque

def solution(priorities: list, location: int):
    print_queue: deque = deque(priorities)
    index_queue: deque = deque([i for i in range(len(priorities))])

    result: list = []

    while print_queue:
        is_changed: bool = False
        
        val: int = print_queue.popleft()
        idx: int = index_queue.popleft()

        for i in print_queue:
            if val < i:
                is_changed = True
                break
        
        if is_changed:
            print_queue.append(val)
            index_queue.append(idx)

        else:
            result.append(idx)

    answer: int = result.index(location) + 1
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([2, 1, 3, 2], 2))