
def inputNum() :
    myNum = int(input())
    count = myNum - 1
    myNumList = list(map(int, input().split()))    
    if(myNum != len(myNumList)):
        return '입력이 이상해요'
    
    myNumList.sort()
    newNum = int(input())
    newNumList = list(map(int, input().split()))
    if(newNum != len(newNumList)):
        return '입력이 이상해요'
    
    result = []
    for num in newNumList:
        re = binary(myNumList, 0, count, num)
        result.append(re)

    return result

def binary(arr, first, last, num):
    while(first <= last):
        middle = int((first + last)/2)
        isBigger = num - arr[middle]

        if(isBigger > 0): # 크다
            first = middle + 1
        elif(isBigger < 0): # 작다
            last = middle - 1
        else: # 똑같다
            return 1
        
    return 0 # 없음

result = inputNum()
print(" ".join(map(str, result)))
