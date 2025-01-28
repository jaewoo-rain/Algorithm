# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

import sys
input = sys.stdin.readline

N , M, START = map(int,input().split())
visited = [False] * (N+1)
graph = [[False]*(N+1) for _ in range(N+1)]

for _ in range(M): # 간선 채우기
    i, j = map(int, input().split())
    graph[i][j] = True
    graph[j][i] = True

def dfs(v):
    print(v, end=' ')
    visited[v] = True

    for index in range(1, N+1):
        if graph[v][index] and not visited[index]:
            dfs(index)

def bfs(v):
    q = [v]
    visited[v] = True
    while q:
        current = q.pop(0)
        print(current, end=' ')
        for index in range(1, N+1):
            if graph[current][index] and not visited[index]:
                visited[index] = True
                q.append(index)
                

dfs(START)
print()

visited = [False] * (N+1)
bfs(START)
