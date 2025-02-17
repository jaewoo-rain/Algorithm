# import travel.thailand
# # import travel.thailand.ThailandPackage 불가
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
from travel import * # init all 해야함
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()
# if __main__ 이용해서 외부 모듈 호출 확인 가능

# 모듈 위치 확인방법
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))