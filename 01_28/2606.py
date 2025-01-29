# 0 1 2 3 4 5 6 7
# 1   1     1
# 2 1   1   1
# 3   1
# 4             1
# 5 1 1       1
# 6         1
# 7       1 

N = int(input())
M = int(input())

count = 0
visited = [False] * (N+1)
graph = [[False] * (N+1) for _ in range (N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

def bfs(v):
    global count
    global q
    visited[v] = True
    while len(q) > 0:
        current = q.pop(0)
        count += 1
        for index in range(N+1):
            if graph[current][index] and not visited[index]:
                visited[index] = True
                q.append(index)

q = [1]
bfs(1)
print(count - 1)

# def dfs(v):
#     global count
#     visited[v] = True
#     for index in range(1, N+1):
#         if graph[v][index] and not visited[index]:
#             count += 1
#             dfs(index)

# dfs(1)
# print(count)

