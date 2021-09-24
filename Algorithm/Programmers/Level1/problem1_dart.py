def solution(dartResult):
    answer: int = 0
    
    result: list = [0 for _ in range(3)]
    
    count: int = 0
    start_index: int = 0
    while start_index != len(dartResult):
        add_index: int = 2
        command: str = dartResult[start_index:start_index + 2]

        if command[1] == '0':
            command = dartResult[start_index:start_index + 3]
            add_index += 1
        
        target_int: int = int(command[0:len(command) - 1])
        target_command: str = command[-1]
        if target_command == 'D':
            target_int = target_int ** 2
        elif target_command == 'T':
            target_int = target_int ** 3
        
        start_index += add_index
        result[count] = target_int

        if start_index == len(dartResult):
            break

        addition_command: str = dartResult[start_index]
        if addition_command == '*':
            for i in range(count, max(-1, count - 2), -1):
                result[i] *= 2
        
        elif addition_command == '#':
            result[count] *= -1

        else:
            start_index -= 1
        
        start_index += 1
        count += 1

    answer = sum(result)
    return answer

print(solution('1D2S3T*'))