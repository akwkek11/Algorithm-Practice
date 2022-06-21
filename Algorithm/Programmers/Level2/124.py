def solution(n: int) -> str:
    number_dict: dict[int, str] = {0: '1', 1: '2', 2: '4'} 
    number_list: list[int] = [1]
    three_list: list[int] = [3 ** i for i in range(18)]
    for i in range(1, 18):
        number_list.append(number_list[-1] + three_list[i])
    
    max_num: int = 0
    for i in range(len(number_list)):
        if n < number_list[i]:
            max_num = i
            break
    
    number_result: list[int] = ['0' for _ in range(max_num)]
    for i in range(max_num - 1, -1, -1):
        number_index: int = (n - number_list[i]) // three_list[i]
        number_result[i] = number_dict[number_index]
        n -= three_list[i] * (number_index + 1)

    return ''.join(number_result[::-1])
    

solution(3)
solution(12)
solution(13)
solution(39)