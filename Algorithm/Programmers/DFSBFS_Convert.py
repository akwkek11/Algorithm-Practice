import copy
from collections import deque

is_visited: list = []
extend_words: list = []
bfs_queue: deque = deque(())

def BFS(start: str, start_index: int) -> None:
    global is_visited
    global extend_words
    global bfs_queue

    same: int = 0

    start_list: list = list(start)
    for i in range(len(extend_words)):
        check_list: list = list(extend_words[i])
        for j in range(len(start_list)):
            if start_list[j] == check_list[j]:
                same += 1

        if same == len(start_list) - 1 and is_visited[i] == 0:
            is_visited[i] = is_visited[start_index] + 1
            bfs_queue.append((extend_words[i], i))
        
        same = 0

def solution(begin, target, words):
    global is_visited
    global extend_words
    global bfs_queue

    answer: int = 0

    extend_words = copy.deepcopy(words)
    extend_words.append(begin)
    is_visited = [0 for _ in range(len(extend_words))]
    
    bfs_queue.append((begin, len(extend_words)-1))
    is_visited[len(extend_words)-1] = 1
    final_index: int = -1
    while bfs_queue:
        word, index = bfs_queue.popleft()
        if word == target:
            final_index = index
            break
        else:
            BFS(word, index)

    if final_index == -1:
        pass
    else:
        answer = is_visited[final_index] - 1

    return answer

# print(f'{solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])}')