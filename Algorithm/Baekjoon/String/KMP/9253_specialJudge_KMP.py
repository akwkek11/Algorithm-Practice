import sys

def KMPSearch(target: str, pattern: str) -> int:
    M: int = len(pattern)
    N: int = len(target)

    lps: list = [0 for _ in range(M)]

    computeLPS(pattern, lps)

    i: int = 0
    j: int = 0
    while i < N:
        if pattern[j] == target[i]:
            i += 1
            j += 1
        elif pattern[j] != target[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            return i-j

    return float('inf')
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
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

A: str = str(sys.stdin.readline().strip())
B: str = str(sys.stdin.readline().strip())
target: str = str(sys.stdin.readline().strip())
print('YES') if KMPSearch(A, target) != float('inf') and KMPSearch(B, target) != float('inf') else print('NO')