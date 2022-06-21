import sys

T: int = int(sys.stdin.readline().strip())

def dfs(reverse_str: str) -> None:
    temp: list = now_word_list[:]
    temp.sort()
    if temp == now_word_list:
        if len(reverse_str) == len(word_list):
            print(reverse_str)
            return 1
        for i in ['0', '1']:
            if i == '0':
                now_word_list.append(word_list[len(reverse_str)])
            else:
                now_word_list.append(word_list[len(reverse_str)][::-1])
            result: int = dfs(reverse_str + i)
            if result:
                return 1
            now_word_list.pop()
    return 0

for _ in range(T):
    N: int = int(sys.stdin.readline().strip())
    word_list: list = []
    now_word_list: list = []
    for _ in range(N):
        word_list.append(sys.stdin.readline().strip())
    for i in ['0', '1']:
        if i == '0':
            now_word_list.append(word_list[0])
        else:
            now_word_list.append(word_list[0][::-1])
        result: int = dfs(i)
        if result:
            break
        now_word_list.pop()