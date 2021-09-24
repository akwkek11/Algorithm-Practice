import heapq
from collections import deque

def solution(enter: list, leave: list) -> list:
    '''
        2021-09-13, https://programmers.co.kr/learn/courses/30/lessons/86048?language=python3
        문제 : 입실 퇴실
    '''
    # 사람 수 변수
    num_people: int = len(enter)

    # 1번부터 n번까지 만난 횟수 저장, 처음은 slicing으로 자를 것
    answer: list = [0 for _ in range(num_people + 1)]

    # 나가는 index에 따라서 min_heap 사용
    people_heap: heapq = []
    
    # 들어올 사람, 나갈 사람 queue
    enter_queue: deque = deque(enter)
    leave_queue: deque = deque(leave)

    # 각 사람이 나가는 순서 저장
    leave_index: dict = {}
    for index, value in enumerate(leave):
        leave_index[value] = index
    
    # enter_queue에 있는 사람을 한 명 씩 넣고, 다음 사람이 들어오기 전까지
    # 나갈 순서에 해당하는 사람들은 전부 내보내는 방식
    while leave_queue:
        if enter_queue:
            next_people: int = enter_queue.popleft()
            for index, value in people_heap:
                answer[value] += 1
            answer[next_people] += len(people_heap)
            heapq.heappush(people_heap, (leave_index[next_people], next_people))

        while people_heap:
            now_people: int = leave_queue.popleft()
            heap_people: tuple = heapq.heappop(people_heap)

            if now_people != heap_people[1]:
                leave_queue.appendleft(now_people)
                heapq.heappush(people_heap, (leave_index[heap_people[1]], heap_people[1]))
                break

    # 0번째 사람은 없으므로 slicing 사용
    return answer[1:]

print(solution([1,4,2,3], [2,1,3,4]))
print(solution([3,2,1], [2,1,3]))
print(solution([1,4,2,3], [2,1,4,3]))