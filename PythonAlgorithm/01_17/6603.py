# 받은 숫자들 중에서
# 6개를 뽑기, 순서 상관없음
# 첫 번째 수는 k (6 < k < 13)
# 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.
# 입력의 마지막 줄에는 0이 하나 주어진다. 
# 0 나오기전까지는 여러개 가능함

'''
표준 입력에서 데이터를 한 줄씩 읽는다.
각 줄을 파싱하여 k와 S를 분리.
줄이 0인 경우 종료.
S에서 가능한 크기 6의 조합을 백트래킹으로 생성.
시작 인덱스, 깊이, 현재 경로, 결과를 매개변수로 하는 재귀 함수 설계.
깊이가 6이 되면 현재 경로를 결과 리스트에 추가.
S의 원소를 하나씩 선택하면서 재귀 호출.
각 테스트 케이스 결과를 사전순으로 포맷팅하여 저장.
테스트 케이스 간 결과를 빈 줄로 구분하여 출력.
'''

import sys

def backtrack(start, depth, path, S, results):
    if depth == 6:
        results.append(path[:])
        return

    for i in range(start, len(S)):
        path.append(S[i])
        backtrack(i + 1, depth + 1, path, S, results)
        path.pop()


input = sys.stdin.read
data = input().strip().split("\n")

results = []
for line in data:
    if line == "0":
        break
    
    nums = list(map(int, line.split()))
    k = nums[0]
    S = nums[1:]
    
    if len(S) != k:
        continue

    test_case_results = []
    backtrack(0, 0, [], S, test_case_results)

    results2 = []
    for value in test_case_results:
        results2.append(" ".join(map(str, value)))
    results.append("\n".join(results2))

print("\n\n".join(results))


