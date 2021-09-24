from collections import Counter, defaultdict

def solution(n, results):
    win_dict: defaultdict = defaultdict(list)
    lose_dict: defaultdict = defaultdict(list)
    for winner, loser in results:
        win_dict[loser].append(winner)
        lose_dict[winner].append(loser)

    print(win_dict)
    print(lose_dict)
    total_count: list = [0 for _ in range(n + 1)]
    for winner, loser in results:
        for i in win_dict[winner]:
            total_count[i] += 1

        for i in lose_dict[loser]:
            total_count[i] += 1

    print(total_count)
    count: Counter = Counter(total_count)
    return count[n - 1]

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))