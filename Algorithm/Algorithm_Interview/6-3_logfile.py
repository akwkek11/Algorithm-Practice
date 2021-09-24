def sorting(log_list: list) -> list:
    number_list: list = []
    alpha_list: list = []

    for i in log_list:
        if i.split()[1].isdigit():
            number_list.append(i)
        else:
            alpha_list.append(i)
    
    alpha_list.sort(key=lambda x:(x.split()[1:], x.split()[0]))
    return alpha_list + number_list

print(f'{sorting(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])}')