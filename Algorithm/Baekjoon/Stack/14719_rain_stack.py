import sys

def stack_simulation(block: list, st: list) -> None:
    res: int = 0
    while block:
        next_block: int = block.pop()

        if not st:
            pass
        else:
            while st:
                st_top: int = st.pop()
                target: int = st_top
                if st:
                    target = st[0]
                
                if next_block >= target:
                    res += min(next_block, target) - st_top
                else:
                    st.append(st_top)
                    break
        
        st.append(next_block)

    return res

H, W = map(int, sys.stdin.readline().strip().split())

block_map: list = list(map(int, sys.stdin.readline().strip().split()))
stack: list = []

count: int = 0

count += stack_simulation(block_map, stack)
count += stack_simulation(stack, block_map)

print(f'{count}')

