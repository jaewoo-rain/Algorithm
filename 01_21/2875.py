# 여자:남자 = 2:1
# 여자 N, 남자 M, 인턴쉽 K

import sys
input = sys.stdin.readline


N,M,k = list(map(int, input().strip().split()))

f = N // 2
m = M

def boo(l):
    if N+M-k >= l * 3:
        print(l)
    else:
        l -= 1
        boo(l)

max_teams = min(f, m)
boo(max_teams)
