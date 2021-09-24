import sys

D: int = int(sys.stdin.readline().strip())
is_find: bool = False

for D in range(9, 10000, 9):
    for i in range(0, 1000000):
        res: int = i - int(''.join(list(reversed(str(i)))))
        if res == D:
            print(f'{D} : {i}')
            is_find = True
            break
    
    '''
    if not is_find:
        print('-1')
    '''
    
    is_find = False
