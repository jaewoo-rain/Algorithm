# 인풋 데이터를 n,k받고 리스트 형식으로 arr받기
# arr의 마지막부터 하나씩 돌면서 몫과 나머지를 구한다
# 나머지가 0이되면 바로 리턴한다
# 결과값은 result 변수에 저장한다

import sys
input = sys.stdin.readline

n, k = list(map(int,input().strip().split()))
result = 0
arr =[]
for _ in range(n):
    arr.append(int(input()))

for index in range(len(arr)-1, -1, -1):
    result += k // arr[index] # 몫
    k = k % arr[index]
    if k == 0:
        break

print(result)
