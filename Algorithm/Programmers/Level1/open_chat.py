from collections import defaultdict

def solution(record):
    uid_dict: defaultdict = defaultdict(str)
    answer: list = []

    # mapping uid - nickname
    for log in record:
        log_parser: list = log.split(' ')
        if (log_parser[0] == 'Enter' and uid_dict[1] == '') or log_parser[0] == 'Change':
            uid_dict[log_parser[1]] = log_parser[2]
    
    # save log
    for log in record:
        log_parser: list = log.split(' ')
        if log_parser[0] == 'Enter':
            answer.append(f"{uid_dict[log_parser[1]]}님이 들어왔습니다.")
        elif log_parser[0] == 'Leave':
            answer.append(f"{uid_dict[log_parser[1]]}님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))