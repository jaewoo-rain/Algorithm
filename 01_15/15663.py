# 동일 배열 내에 중복 확인 : 'in 키워드', 'count()사용', 'set 자료구조'

# set함수를 사용할경우 순서가 섞임
# 순서를 유지하며 중복을 제거하려면 dict.fromkeys() 또는 반복문 사용용

# 또는 sorted 사용하기 / sort사용하기에는 set이 리스트가 아니므로 사용 불가
# 또는 list()로 배열을 만든 후 sort사용하기

# if value in lst로 중복을 방지하고 있습니다. 이 방식은 리스트(lst)의 길이가 길어질수록 중복 검사에 시간이 더 걸릴 수 있습니다.
# set()할수를 사용하여 사용된값 used같은 형식으로 만들어 if value in used 사용하기

# set() 함수의 합집합 : |, 교집합 : &

# 딕셔너리와 set()의 차이점
# 딕셔너리는 {key:value}
# set함수는 {value}

# 다음 넘어갈때 리스트 중 사용된 값을 뺀다
# 최종 리스트들 끼리 동일하지 않게 만든다

# 1. 입력 N,M
# 2. 정답 조건 선택한 길이(n)과 M이 동일할 때 까지
# 3. 사용할 자료구조 - 중복을 없애기위해 set() 사용
# 4. 방문 유무 체크를 위한 visited 변수
# 5. 재귀를 이용하여 백트래킹 사용
# 6. 받을 배열의 값 별로 방문유무를 체크하기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().strip().split()))

arr.sort()
result = set()
visited = [False] * N 

def searchAn(n, lst):
    if n == M: 
        result.add(tuple(lst))  # 리스트형식은 set에 추가 못함함
        return
    
    for i in range(N):
        if visited[i]:  # 이미 방문한 값은 스킵
            continue
        visited[i] = True
        searchAn(n + 1, lst + [arr[i]])
        visited[i] = False

searchAn(0, [])
for value in sorted(result):  # 정렬하여 출력
    print(*value)
