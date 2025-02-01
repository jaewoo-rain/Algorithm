# N × M 크기의 미로가 주어짐
# 1 -> 이동할 수 있는 칸, 0 -> 이동할 수 없는 칸
# (1,1)에서 출발하여 (N,M)까지 가는 최소 칸 수를 출력
# 이동할 때 상하좌우로 이동 가능
# 항상 도착할 수 있는 입력만 주어짐

# 미로는 상하좌우로 이동 가능
# 이를 위해 dx, dy 리스트를 설정

# 위쪽(x, y+1)
# 아래쪽(x, y-1)
# 오른쪽(x+1, y)
# 왼쪽(x-1, y)

# 미로와 크기 입력 받기
# 이동할 방향 정의
# BFS 탐색 시작
# 현재 위치에서 이동 가능한 위치 탐색
# 최종 결과 출력

# 입력 받기: 미로의 크기(N×M)와 미로의 정보를 입력받는다.
# 이동 방향 정의: 상, 하, 좌, 우 4방향으로 이동할 수 있도록 dx, dy 리스트를 정의한다.
# BFS 탐색: (1,1)에서 출발하여 (N,M)까지 이동하면서 최소 칸 수를 기록한다.
# 결과 출력: (N,M)까지 도달했을 때의 값을 출력한다.

# 큐에 시작점 (0,0) 추가
# 큐에서 하나씩 꺼내면서 위, 아래, 오른쪽, 왼쪽 이동
# 이동할 수 있는 칸이면 거리 증가 후 다시 큐에 추가
# 도착 지점(N-1, M-1)에 도달하면 거리 출력

# from collections import deque

# def bfs(maze, n, m):
#     # 이동 방향 정의 (오른쪽, 왼쪽, 위, 아래)
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]

#     # BFS 탐색을 위한 큐 생성 및 시작 지점 (0,0) 추가
#     queue = deque([(0, 0)])

#     while queue:
#         x, y = queue.popleft()  # 현재 위치 (x, y) 가져오기
        
#         # 네 방향(오른쪽, 왼쪽, 위, 아래)으로 이동
#         for i in range(4):
#             nx = x + dx[i]  # 새로운 x 좌표
#             ny = y + dy[i]  # 새로운 y 좌표
            
#             # 미로 범위 내에 있고, 이동할 수 있는 곳(1)이라면
#             if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
#                 # 최단 거리 갱신
#                 maze[nx][ny] = maze[x][y] + 1
#                 queue.append((nx, ny))  # 큐에 추가하여 다음 탐색 진행

#     # 도착 지점 (N-1, M-1)까지의 최단 거리 반환
#     return maze[n-1][m-1]

# n, m = map(int, input().split())
# maze = [list(map(int, input().strip())) for _ in range(n)]

# print(bfs(maze, n, m))

from collections import deque

def bfs(maze, n, m):
    # n-1, m-1 도착지
    
    # 이동방향 정의
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(0,0)])

    while queue:
        x,y = queue.popleft() # 현재위치

        for i in range(4): # 4방향으로 이동 시도
            newX = x + dx[i]
            newY = y + dy[i]
            
            if 0 <= newX <n and 0 <= newY < m: # 미로안의 범위에 존재할때
                if maze[newX][newY] == 1: # 미로에 값이 존재한다면
                    maze[newX][newY] = maze[x][y] + 1 # 이동하여 값 증가
                    queue.append((newX,newY))
        
    return maze[n-1][m-1]


n,m = map(int, input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]

print(bfs(maze, n, m))

왼쪽(appendleft()), 오른쪽(append()) 추가
