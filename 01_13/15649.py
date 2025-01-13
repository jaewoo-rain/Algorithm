# 입력
# 4 2

# 출력
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3
# --------------

# 1. 입력 N,M
# 2. 정답 조건 선택한 길이(n)과 M이 동일할 때 까지
# 3. N을 순회하며 방문 유무 체크 후 재귀를 이용
# 4. 재귀 이후 방문 유무 다시 돌리고, 정답에 넣는 리스트도 원상복귀하기


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []    # 정답 리스트
visited = [False] * (N+1) # 중복확인을 위한 리스트

def recur(n, lst):
    # 종료 조건
    if n == M:
        arr.append(lst)
        return
    
    # 하부 함수 호출
    for i in range(1, N+1):
        if visited[i] == False: # 선택하지 않았을 경우
            visited[i] = True
            recur(n+1, lst+[i])
            visited[i] = False

recur(0, [])
for lst in arr:
    print(*lst)
