import sys

# Euclidean Algorithm - Extend
def ext_euc(a: int, b: int) -> tuple:
    if b == 0:
        return a, 1, 0
    g, x, y = ext_euc(b, a%b)
    return g, y, x-(a//b)*y

T: int = int(sys.stdin.readline().strip())

def ceil(a, b) -> float:
    if a >= 0:
        return (a + b - 1) // b
    return a // b

for _ in range(T):
    k, c = map(int, sys.stdin.readline().strip().split())
    x, y, z = ext_euc(k, c)
    
    z = (z % k + k) % k
    if x != 1 or z > 10 ** 9:
        print('IMPOSSIBLE')
        continue
    
    if c == 1:
        print('IMPOSSIBLE') if k + 1 > 10 ** 9 else print(f'{k + 1}')
        continue

    if k == 1:
        print('1')
        continue
    
    print(f'{z}')