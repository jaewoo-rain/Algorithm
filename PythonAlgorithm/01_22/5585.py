# 380 
# -> 1000 - 380 = 620
# -> 500*1 + 100*1 + 10*2
# -> 1+1+2 = 4
import sys
input = sys.stdin.readline

price = int(input())
pay = 1000
result = 0
coins = [500, 100, 50, 10, 5, 1]
change_money = pay - price

for coin in coins:
    result += change_money // coin
    change_money = change_money % coin

print(result)