from random import *
print(random()) # 0.0 ~ 1.0랜덤 값
print(int(random() * 10) + 1) # 1 ~ 10 사이

print(int(random() * 45) + 1) # 1 ~ 45 이하의 값 생성
print(randrange(1,46)) # 1 ~ 46 미만의 값 생성
print(randint(1,45) )# 1 ~ 45 이하의 값 생성

print('오프라인 스터디 모임 날짜는 매월 ' + str(randint(4,28)) +'일로 선정되었습니다.')