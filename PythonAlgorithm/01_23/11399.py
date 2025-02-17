# a1 + (a1+a2) + (a1+a2+a3) + (a1+a2+a3+a4)
# 가장 짧은 시간부터 더해 나간다

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    times = list(map(int, input().strip().split()))
    if len(times) != N:
        return '잘못 입력했어요'
    times.sort()

    result = 0
    value = 0
    for time in times:
        value += time
        result += value
    print(result)

main()