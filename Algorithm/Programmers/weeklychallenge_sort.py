def solution(weights: list, head2head: list) -> list:
    # 답
    answer: list = []
    
    # (승률, 무거운 사람 이긴 횟수, 플레이어 무게, 플레이어 인덱스)
    player_list: list = []
    
    # n번째 플레이어 조회 인덱스
    player_idx: int = 0
        
    # player_list에 append
    for player_match in head2head:
        win: int = 0
        lose: int = 0
        win_heavy: int = 0
        for idx in range(len(player_match)):
            if player_match[idx] == 'W':
                win += 1
                if weights[idx] > weights[player_idx]:
                    win_heavy += 1
            elif player_match[idx] == 'L':
                lose += 1

        # N을 제외한 W, L만 카운트해서 계산, 0으로 나누어질 것을 대비하여 max로 분모의 최소는 1로 고정.
        player_list.append((win/(max(win + lose, 1)), win_heavy, weights[player_idx], player_idx))

        # 다음 플레이어 조회
        player_idx += 1
    
    '''
        로직에 따르면, 승률이 높은 순서
        승률이 동일하다면 무거운 사람을 이긴 횟수가 많은 순으로
        2개가 동일하다면 몸무게가 무거운 순으로
        3개가 동일하다면 작은 번호가 앞쪽이니

        높은 순서로 배열하기 위해선 -를 붙이고
        낮은 순서로 배열하기 위해선 -를 붙이지 않는 식으로 처리.
    '''
    player_list.sort(key = lambda x : (-x[0], -x[1], -x[2], x[3]))
    for i in player_list:
        answer.append(i[3] + 1)
    return answer

print(solution([50, 82, 75, 120], ["NLWL","WNLL","LWNW","WWLN"]))
print(solution([145,92,86], ["NLW","WNL","LWN"]))
print(solution([60,70,60], ["NNN","NNN","NNN"]))