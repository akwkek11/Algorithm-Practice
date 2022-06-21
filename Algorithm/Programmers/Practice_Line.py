import math

def solution(n: int, k: int) -> list:
    answer: list = []
    num_list: list = [i for i in range(1, n + 1)]
    
    k -= 1
    while k > 0:
        answer.append(num_list[k // math.factorial(max(0, len(num_list) - 1))])
        del num_list[k // math.factorial(max(0, len(num_list) - 1))]
        k %= math.factorial(max(0, len(num_list)))
    
    while num_list:
        answer.append(num_list[0])
        del num_list[0]
    return answer

print(solution(3, 5))
print(solution(4, 1))
print(solution(4, 20))
print(solution(5, 25))
print(solution(6, 241))