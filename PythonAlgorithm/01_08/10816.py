from bisect import bisect_left, bisect_right

def bisectCount(sortList, value):
    start = bisect_left(sortList, value)
    end = bisect_right(sortList, value)
    return end - start

def main():
    n = int(input().strip())
    nList = list(map(int, input().strip().split())) 
    nList.sort()

    m = int(input().strip()) 
    mList = list(map(int, input().strip().split())) 
    
    
    # 각 값을 계산하여 결과 저장
    result = [bisectCount(nList, value) for value in mList]
    print(" ".join(map(str, result)))

main()