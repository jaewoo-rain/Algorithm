# 그리디 알고리즘
# 1. 현재의 선택이 미래의 선택에 영향을 주지 않는경우
# ex) 서울 - 대전 - 부산 여행시
# 서울에서 대전 최소 비용 선택, 대전에서 부산 최소비용 선택
# 이때 서울에서 대전을 가는 방법을 선택할때 대전에서 부산을 가는 방법에 영향을 주지 않음

# 2. 부분의 최적해가 모이면 전체의 최적해가 될때때
# 서울에서 대전까지의 비용 + 대전에서 부산까지의 비용
# 부분 + 부분 = 전체

# 문제 풀이 시
# 어떻게 정렬을 할것인가?
# 어떻게 해야 현재의 선택이 미래의 선택에 영향을 주지 않도록 정렬할 수 있을까

# Q = 25
# D = 10
# N = 5
# P = 1
# 거스름돈 < 500

# if 124:
#     Q * 4 = 100
#     D * 2 = 20
#     N * 0 = 0
#     P * 4 = 4

import sys
input = sys.stdin.readline

# 입력 횟수를 받을 변수 설정
freq = int(input().strip())

# for문을 이용해서 입력 횟수만큼 저장
# 각 값을 리스트 형식으로 저장
# 엔터키로 구분
lst = []
for _ in range(freq):
    lst.append(int(input().strip()))


# 거스름돈
COIN = [25, 10, 5, 1]

# lst에 존재하는 값들을 하나씩 거스름돈 만들기
# 거스름 돈의 단위가 큰 순서대로 나누어 몫과 나머지 구하기
# 나머지를 이용해 다음 단위로 나누기

for value in lst:
    result = []
    for coin in COIN:
        q = value // coin
        value = value % coin
        result.append(q)
    print(*result)