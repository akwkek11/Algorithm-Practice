from typing import List

def solution(land: List[List[int]]) -> int:
    save: List[List[int]] = [[0 for _ in range(4)] for _ in range(len(land))]
    save[0] = land[0][:]
    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                if j != k:
                    save[i][j] = max(save[i - 1][k] + land[i][j], save[i][j])
    
    return max(save[-1])