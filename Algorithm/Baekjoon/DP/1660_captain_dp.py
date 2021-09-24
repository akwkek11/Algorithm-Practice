import sys
sys.setrecursionlimit(10000)

def dfs(number: int) -> int:
    if number == 0:
        return 0
    
    if n_map[number] != -1:
        return n_map[number]
    
    min_num = float('inf')
    
    for i in range(len(triangle)):
        if triangle[i] > number:
            break

        min_num = min(min_num, 1 + dfs(number - triangle[i]))
    
    return min_num

triangle: list = [1]
for i in range(2, 200):
    plus: int = (i * (i + 1)) // 2
    triangle.append(triangle[-1] + plus)

N: int = int(sys.stdin.readline().strip())
n_map: list = [-1 for _ in range(N+1)]

for i in range(1, N+1):
    n_map[i] = dfs(i)

print(f'{n_map[N]}')