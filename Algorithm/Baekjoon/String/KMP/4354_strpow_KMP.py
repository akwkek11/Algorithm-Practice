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

    print(lps)
    return lps[-1]

for _ in range(11):
    input_str: str = str(sys.stdin.readline().strip())
    if input_str == '.':
        break
    
    res_value: int = computeLPS(input_str)
    res_value = 1 if res_value != 0 and len(input_str) % (len(input_str) - res_value) != 0 else len(input_str) // (len(input_str) - res_value)

    print(f'{res_value}')