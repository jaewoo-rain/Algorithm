# 1. 제일 작은 길이의 랜선을 찾아서 그 길이 만큼 잘라본다
# 1-1. 자르는건 값을 나눈다? -> 나누어진 몫의 합을 N과 비교한다다
# 2. 더 많은 랜선이 필요하다만 길이를 1씩 줄이며 잘라본다

# def cuttingLen(arr, n):
#     k = len(arr)
#     arr.sort()
#     small = arr[0] + 1

#     result = 0
#     while result < n:
#         result = 0
#         small -= 1
#         for value in arr:
#             result += value // small
#     print(small)

# def main():
#     k, n = map(int, input().split())
#     lens = []
#     for i in range(k):
#         value = int(input())
#         lens.append(value)

    
#     cuttingLen(lens, n)


# main()


def cuttingLen(arr, n):
    lo, high = 1, max(arr)
    best = 0

    while lo <= high:
        mid = (lo + high) // 2  
        total = 0
        for value in arr: 
            pieces = value // mid 
            total += pieces

        if total >= n:
            best = mid 
            lo = mid + 1 
        else: 
            high = mid - 1 

    return best

def main():
    k, n = map(int, input().split())
    lens = []
    for _ in range(k):
        value = int(input())
        lens.append(value)

    result = cuttingLen(lens, n)
    print(result)

main()