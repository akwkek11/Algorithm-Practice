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
 
def solve(a, b):
    #gcd, y, x
    g, x, y = ext_euc(a, b)

    if g != 1:
        return -1
    else:
        # no minus
        return y if y > 0 else (y+a)%a
 
n, a= map(int, input().split())

add_inverse = n-a
mul_inverse = solve(n, a)

print(f'{add_inverse} {mul_inverse}')