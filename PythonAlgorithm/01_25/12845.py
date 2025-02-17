import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().strip().split()))

max_level = max(n_list)

# 최대값 하나 제거
n_list.remove(max_level)

result = 0
for level in n_list:
    result += max_level+level

print(result)               