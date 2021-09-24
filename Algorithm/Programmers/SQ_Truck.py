from collections import deque

def solution(bridge_length: int, weight: int, truck_weights: list) -> int:
    answer: int = 0
    bridge: deque = deque([0 for _ in range(bridge_length)])
    truck: deque = deque(truck_weights)

    now_weight: int = 0
    now_truck: int = truck.popleft()
    now_weight += now_truck
    bridge.popleft()
    bridge.append(now_truck)
    answer += 1

    is_first: bool = True
    while now_weight != 0:
        out_truck: int = bridge.popleft()
        answer += 1
        if is_first or out_truck != 0:
            is_first = False
            now_weight -= out_truck
            while truck:
                now_truck: int = truck.popleft()
                now_weight += now_truck

                if now_weight <= weight:
                    bridge.append(now_truck)
                    if len(bridge) > bridge_length:
                        out_truck = bridge.popleft()
                        now_weight -= out_truck
                        answer += 1

                else:
                    truck.appendleft(now_truck)
                    if len(bridge) < bridge_length:       
                        bridge.append(0)
                    now_weight -= now_truck
                    break
        else:
            bridge.append(0)

    return answer

print(solution(1, 2, [1, 1, 1]))
print(solution(1, 1, [1, 1, 1]))
print(solution(4, 2, [1, 1, 1, 1]))
print(solution(3, 3, [1, 1, 1]))
print(solution(3, 1, [1, 1, 1]))
print(solution(5, 5, [1, 1, 1, 1, 1, 2, 2]))
print(solution(7, 7, [1, 1, 1, 1, 1, 3, 3]))
print(solution(5, 5, [1,1,1,1,1,2,2,2,2]))