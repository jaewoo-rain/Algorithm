
def inputEvent():
    N = int(input())
    NList = list(map(int, input().split()))
    if(len(NList) != N):
        return '똑바로 적으세요'
    NList.sort()

    M = int(input())
    MList = list(map(int, input().split()))
    if(len(MList) != M):
        return '똑바로 적으세요'
    
    for value in MList:
        result = binarySearch(NList, value)
        print(result)

def binarySearch(arr, val):
    first, last = 0, len(arr)-1

    while(first <= last):
        middle = (first + last) // 2
        isBigger = val - arr[middle]
        if(isBigger > 0):
            first = middle + 1
        elif(isBigger < 0):
            last = middle - 1
        else:
            return 1
    return 0

inputEvent()