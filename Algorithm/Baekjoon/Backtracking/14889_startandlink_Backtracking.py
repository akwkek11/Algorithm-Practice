from itertools import combinations

import sys

N: int = int(sys.stdin.readline().strip())
player_list: list = [i for i in range(N)]
score_list: list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

my_team_score: int = 0
versus_score: int = 0
minimum: int = float('inf')

possible_combinations: list = list(combinations(player_list, N // 2))
check: list = [i for i in possible_combinations if i[0] == 0]
check_versus: list = list(reversed([i for i in possible_combinations if i[0] != 0]))

while check or check_versus:
    next_target: tuple = check.pop()
    next_versus: tuple = check_versus.pop()
    
    for i in next_target:
        for j in next_target:
            my_team_score += score_list[i][j]

    for i in next_versus:
        for j in next_versus:
            versus_score += score_list[i][j]

    minimum = min(minimum, abs(my_team_score - versus_score))
    my_team_score = versus_score = 0
    if minimum == 0:
        break
    
print(f'{minimum}')