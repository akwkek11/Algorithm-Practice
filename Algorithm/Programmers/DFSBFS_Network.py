from collections import deque

is_visited: list = []
bfs_queue: deque = deque()

def BFS(x: int, computer_map: list) -> None:
    global is_visited
    global bfs_queue
    for i in range(len(is_visited)):
        if computer_map[x][i] == 1 and is_visited[x][i] == 0:
            is_visited[x][i] = 1
            bfs_queue.append(i)

def solution(n, computers):
    global is_visited
    is_visited = [[0 for _ in range(n)] for _ in range(n)]
    answer: int = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and is_visited[i][j] == 0:
                answer += 1
                bfs_queue.append(j)
                is_visited[i][j] = 1
                while bfs_queue:
                    target_x = bfs_queue.popleft()
                    BFS(target_x, computers)
    return answer