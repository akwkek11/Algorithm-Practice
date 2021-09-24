import sys

# KMP
def computeLPS(pattern: str) -> list:
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
    print(lps)
    return lps

s: str = str(sys.stdin.readline().strip())
max_len: int = -1
while len(s) >= 1:
    max_len = max(max_len, max(computeLPS(s)))
    s = s[1:] if len(s) > 1 else ''

    if max_len >= len(s):
        break
print(f'{max_len}')