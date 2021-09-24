def solution(prices: list) -> list:
    answer: list = []
    save_stack: list = []

    while prices:
        now: int = prices.pop()
        if not save_stack:
            save_stack.append(now)
            answer.append(0)
        
        else:
            count: int = 0
            for i in range(len(save_stack)-1, -1, -1):
                count += 1
                if save_stack[i] < now:
                    break
            
            save_stack.append(now)
            answer.append(count)

    return answer[::-1]

print(solution([1, 3, 5, 4, 2, 3, 1, 3]))