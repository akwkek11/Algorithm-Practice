'''
    Euclidean
    while(a!=b):
        if(a>b) : a-=b
        else    : b-=a
'''

def ext_euc(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_euc(b, a%b)
    return g, y, x-(a//b)*y
 
def solve(a, b, s):
    if a == 0 and b == 0:
        return s == 0
    if a == 0:
        return s % b == 0
    if b == 0:
        return s % a == 0
    g, x, y = ext_euc(a, b)
    if s % g != 0:
        return False
    x *= s // g
    y *= s // g
    for k in range(-g*x//b+1, g*y//a+1):
        if ext_euc(x + k*b//g, y - k*a//g)[0] == 1:
            return True
    return False
 
a, b, s = map(int, input().split())
print("YES" if solve(a, b, s) else "NO")