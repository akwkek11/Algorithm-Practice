N: int = int(input())
def dfs(number_string: str) -> None:
    length: int = len(number_string)
    if length >= 2:
        for i in range(1, length // 2 + 1):
            if number_string[length - 2*i:length - i] == number_string[length - i: length]:
                return 0

    if length == N:
        print(number_string)
        exit(0)

    for i in '123':
        if i != number_string[-1]:
            dfs(number_string + i)

for i in '123':
    result: int = dfs(i)