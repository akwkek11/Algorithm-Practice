from collections import defaultdict

def solution(tickets):
    answer: list = []
    travel_dict: defaultdict = defaultdict(list)

    for i in tickets:
        travel_dict[i[0]].append(i[1])
    
    for key, value in travel_dict.items():
        travel_dict[key].sort(reverse = True)

    q = ["JFK"]
    while q:
        next_target: str = q[-1]
        if not travel_dict[next_target]:
            answer.append(q.pop())
        else:
            q.append(travel_dict[next_target].pop())

    answer = answer[::-1]
    return answer

print(f'{solution([["JFK", "B"], ["B", "JFK"], ["JFK", "A"], ["A", "D"], ["D","A"]])}')