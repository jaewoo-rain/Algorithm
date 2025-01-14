# 1. 입력 N, M
# 2. 종료 조건 n(깊이) == M
# 3. 중복가능
# 4. 하부조건 없음

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [] # 출력 배열열

def choise(n, lst):
    if(n == M):
        arr.append(lst)
        # print('종료')
        return
    for i in range(1, N+1):
        choise(n+1, lst + [i])

choise(0, [])
for val in arr :
    print(*val)