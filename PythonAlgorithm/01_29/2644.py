# # 첫째 줄에는 전체 사람의 수 n
# # 둘째 줄에는 촌수를 계산해야하는 두 사람의 번호
# # 셋째 줄에는 부모-자식들 간의 관계의 개수 m
# # 넷째줄부터~
# # 쭉~
# # 부모 자식간의 관계 x,y
# # x는 y의 부모이다
# # 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력

# # 9 -> 전체 사람의 수
# # 7 3 -> 7번과 3번 의 촌수 구하기
# # 7 -> 부모-자식이 7그룹 존재
# # 1 2 
# # 1 3
# # 2 7
# # 2 8
# # 2 9
# # 4 5
# # 4 6

# # 부모-자식 사이는 간선으로 연결
# # 깊이 우선 탐색으로 한곳을 쭉 탐색함

# import sys
# input = sys.stdin.readline

# def dfs(node, count):
#     if node == target2:
#         return count  # 목표 노드를 찾으면 촌수 반환

#     visited[node] = True  # 방문 처리

#     for next in edges[node]:  # 현재 노드와 연결된 노드 탐색
#         if not visited[next]:  # 방문하지 않은 노드만 탐색
#             result = dfs(next, count + 1)  # 촌수 증가
#             if result != -1:
#                 return result  # 찾았으면 촌수 반환

#     return -1  # 끝까지 못 찾으면 -1 반환

# n = int(input())
# target1, target2 = map(int, input().split())
# m = int(input())

# edges = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)

# for _ in range(m):
#     x, y = map(int, input().split())
#     edges[x].append(y)
#     edges[y].append(x)

# result = dfs(target1, 0)
# print(result)


import sys
input = sys.stdin.readline

def bfs(start):
    queue = [(start, 0)]
    front = 0 
    visited[start] = True

    while front < len(queue):
        node, count = queue[front]  # 현재 노드, 촌수
        front += 1  # 큐에서 pop (리스트에서 슬라이싱 대신 인덱스 증가)

        if node == target2:  # 목표 노드 도착하면 촌수 반환
            return count

        for next_node in edges[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, count + 1))

    return -1  # 찾을 수 없으면 -1 반환

# 입력 받기
n = int(input())  # 전체 사람 수
target1, target2 = map(int, input().split())  # 촌수 계산할 두 사람
m = int(input())  # 관계 개수

# 그래프 초기화 (인접 리스트)
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 부모-자식 관계 입력 받기 (양방향)
for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

# BFS 탐색 수행
result = bfs(target1)
print(result)  # 결과 출력