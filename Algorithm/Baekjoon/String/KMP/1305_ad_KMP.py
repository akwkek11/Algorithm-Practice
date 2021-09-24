import sys

# KMP
def computeLPS(pattern: str) -> int:
    length: int = 0
    lps: list = [0 for _ in range(len(pattern))]
    i: int = 1

    count: int = 0
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
    return lps[-1]

L: int = int(sys.stdin.readline().strip())
s: str = str(sys.stdin.readline().strip())
print(f'{L - computeLPS(s)}')