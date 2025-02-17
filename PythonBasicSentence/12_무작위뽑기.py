from random import *
# lst = [1,2,3,4,5]
# shuffle(lst)
# # print(lst)
# print(sample(lst,2)) # lst에서 두개를 무작위로 뽑기

users = range(1, 21) # 1부터 20까지 숫자 생성
# print(type(users)) # range

users = list(users)
# print(type(users)) # list

shuffle(users)
winners = sample(users,4)

print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))


