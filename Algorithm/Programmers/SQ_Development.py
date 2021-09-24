from collections import deque

def solution(progresses: list, speeds: list):
    answer: list = []
    in_progresses: list = progresses[:]
    in_speeds: list = speeds[:]

    while in_progresses:
        while in_progresses[0] < 100:
            in_progresses = [in_progresses[i] + in_speeds[i] for i in range(len(in_speeds))]
        
        q: deque = deque(in_progresses)
        count: int = 0
        while q:
            value: int = q.popleft()
            if value < 100:
                q.appendleft(value)
                break
            
            count += 1
        
        answer.append(count)
        in_speeds = in_speeds[count:]
        in_progresses = in_progresses[count:]
    
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))