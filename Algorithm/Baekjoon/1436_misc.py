import sys

six_map: list = [666]

N: int = int(sys.stdin.readline().strip())

def create_map() -> None:
    temp: int = 0
    count: int = 1
    suffix: int = 0
    is_sixsixsix: bool = False

    while count <= N:
        suffix += 1
        if suffix % 10 != 6:
            six_map.append(suffix * 1000 + 666)
            count += 1
        else:
            temp = suffix * 1000 + 666
            size_count: int = 0
            for i in range(len(str(temp)), 3, -1):
                size_count: int = i
                if temp // (10 ** (size_count - 3)) == 666:
                    is_sixsixsix = True
                    break
                temp %= (10 ** (size_count-1))
                
            if is_sixsixsix:
                is_sixsixsix = False
                temp = ((suffix * 1000 + 666) // (10 ** (size_count - 3))) * (10 ** (size_count - 3))
                for i in range (temp, temp + (10 ** (size_count - 3))):
                    six_map.append(i)
                    count += 1
        
        temp = 0
    pass

create_map()
print(f'{six_map[N-1]}')