from collections import defaultdict, deque
import heapq
import sys

N: int = int(sys.stdin.readline().strip())
road_map: list = []
for _ in range(N):
    road_map.append([int(i) for i in list(sys.stdin.readline().strip())])
color_map: list = [[0 for _ in range(N)] for _ in range(N)]
color_queue: deque = deque()
color: int = 0

map_dict: defaultdict = defaultdict(lambda: defaultdict(lambda: float('inf')))
is_visited = [[0 for _ in range(N)] for _ in range(N)]
distance_queue: deque = deque()
distance_checklist: list = [0]

# 최소거리 구할 다익스트라
def dijkstra(graphs: defaultdict, start: int) -> defaultdict:
    distances: defaultdict = defaultdict(lambda: float('inf'))
    queue: heapq = []
    distances[start] = 0
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graphs[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances

# 몇 번 방인지 체크
def bfs(x: int, y: int, now_color: int, mode: int) -> None:
    dx: list = [-1, 1, 0, 0]
    dy: list = [0, 0, -1, 1]

    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if mode == 0:
                if color_map[next_x][next_y] == 0 and road_map[next_x][next_y] == 1:
                    color_map[next_x][next_y] = now_color
                    color_queue.append((next_x, next_y, now_color))
            elif mode == 1:
                if color_map[next_x][next_y] == color_map[x][y] and is_visited[next_x][next_y] == 0:
                    is_visited[next_x][next_y] = 1
                    color_queue.append((next_x, next_y, now_color))
                    distance_queue.append((next_x, next_y, now_color, 0))

# 거리 계산 BFS
def bfs2(x: int, y: int, now_color: int, distance: int) -> None:
    dx: list = [-1, 1, 0, 0]
    dy: list = [0, 0, -1, 1]

    for i in range(len(dx)):
        next_x: int = x + dx[i]
        next_y: int = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if is_visited[next_x][next_y] == 0:
                if color_map[next_x][next_y] == 0:
                    is_visited[next_x][next_y] = 1
                    distance_queue.append((next_x, next_y, now_color, distance + 1))
                elif color_map[next_x][next_y] != now_color:
                    if map_dict[now_color][color_map[next_x][next_y]] >= distance or map_dict[color_map[next_x][next_y]][now_color] >= distance:
                        map_dict[now_color][color_map[next_x][next_y]] = map_dict[color_map[next_x][next_y]][now_color] = distance

# 1. 방 구분하는 로직
for i in range(N):
    for j in range(N):
        if color_map[i][j] == 0 and road_map[i][j] == 1:
            color += 1
            color_map[i][j] = color
            color_queue.append((i, j, color))
            while color_queue:
                x, y, now = color_queue.popleft()
                bfs(x, y, now, 0)

# 2. 방끼리 거리 계산하는 로직
for i in range(N):
    for j in range(N):
        if color_map[i][j] != 0 and color_map[i][j] not in distance_checklist:
            is_visited = [[0 for _ in range(N)] for _ in range(N)]
            distance_checklist.append(color_map[i][j])
            is_visited[i][j] = 1
            color_queue.append((i, j, color_map[i][j]))
            distance_queue.append((i, j, color_map[i][j], 0))
            while color_queue:
                x, y, now = color_queue.popleft()
                bfs(x, y, now, 1)
            
            while distance_queue:
                x, y, now_color, now_distance = distance_queue.popleft()
                bfs2(x, y, now_color, now_distance)

results: defaultdict = dijkstra(map_dict, 1)
print(results[color_map[N - 1][N - 1]])