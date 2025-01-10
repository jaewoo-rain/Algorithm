# 제일 큰수찾기
# 그 다음수 큰수를 찾으면서 그 차이만큼 1씩 뺀다
# 두번째 큰수를 찾으면 그때부터 2씩 뺀다....
# 1번째 - 2번째 차이 > 가져가려는것 -> 차이*1 = S1
# S(n-1) + (n번째 - (n+1)번째 차이) < 가져가려는것 -> 스탑탑

# import heapq

# def findMaxHeight(heights, M):
#     # Step 1: Max 힙 생성 (음수로 변환하여 Min 힙을 Max 힙처럼 사용)
#     maxHeap = [-h for h in heights]
#     heapq.heapify(maxHeap)

#     total = 0  # 가져간 나무의 총 길이
#     currentHeight = -heapq.heappop(maxHeap)  # 가장 큰 나무 높이
#     count = 1  # 현재 처리된 나무 개수

#     while maxHeap:
#         nextHeight = -heapq.heappop(maxHeap)  # 다음 큰 나무 높이
#         diff = currentHeight - nextHeight
#         woodLayer = diff * count

#         if total + woodLayer >= M:
#             # 필요한 양만큼만 가져가고 종료
#             remaining = M - total
#             return currentHeight - (remaining // count)

#         # 가져간 나무 길이를 누적하고, 처리된 나무 개수를 늘림
#         total += woodLayer
#         currentHeight = nextHeight
#         count += 1

#     # 마지막으로 0까지 계산
#     remaining = M - total
#     return currentHeight - (remaining // count)


# N, M = map(int, input().split())
# heights = list(map(int, input().split()))

# print(findMaxHeight(heights, M))

def findMaxHeight(heights, M):
    first, last = 0, max(heights)
    result = 0

    while first <= last:
        mid = (first + last) // 2  # 현재 절단 높이
        total_wood = sum(max(0, h - mid) for h in heights)  # 잘린 나무의 총합

        if total_wood >= M:  # 필요한 나무 양을 만족하면
            result = mid  # 절단 높이를 기록
            first = mid + 1  # 더 높은 절단 높이를 탐색
        else:
            last = mid - 1  # 절단 높이를 낮춤

    return result


N, M = map(int, input().split())
heights = list(map(int, input().split()))

print(findMaxHeight(heights, M))
