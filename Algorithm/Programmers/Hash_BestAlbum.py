from collections import defaultdict

def solution(genres, plays):
    answer = []
    track_list: defaultdict = defaultdict(list)
    sum_list: list = []
    for i in range(len(genres)):
        track_list[genres[i]].append((i, plays[i]))
    
    for key, value in track_list.items():
        track_list[key] = sorted(track_list[key], key=lambda item: item[1], reverse=True)

    print(track_list)
    
    for key, value in track_list.items():
        plays_sum: int = 0
        for i in value:
            plays_sum += i[1]
        sum_list.append((key, plays_sum))

    sum_list = sorted(sum_list, key=lambda item: item[1], reverse=True)

    # find[0] : key, find[1] : sum
    for find in sum_list:
        count: int = 0
        for song_list in track_list[find[0]]:
            count += 1
            answer.append(song_list[0])
            if count == 2:
                break
    
    #print(answer)
    return answer

#solution(["classic", "pop", "pop", "classic", "classic", "pop", "metal"], [500, 600, 600, 150, 800, 2500, 3000])