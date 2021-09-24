import sys

def KMPSearch(target: str, pattern: str) -> list:
    M: int = len(pattern)
    N: int = len(target)

    lps: list = [0 for _ in range(M)]
    result: list = []

    computeLPS(pattern, lps)

    i: int = 0
    j: int = 0
    while i < N:
        if pattern[j] == target[i]:
            i += 1
            j += 1
        elif pattern[j] != target[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == M:
            result.append(i - j + 1)
            j = lps[j - 1]
            
    return result
def computeLPS(pattern: str, lps: list) -> None:
    length: int = 0

    i: int = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

T: str = str(sys.stdin.readline().strip('\n'))
P: str = str(sys.stdin.readline().strip('\n'))
res_list: list = KMPSearch(T, P)

print(f'{len(res_list)}')
for i in res_list:
    print(f'{i}')