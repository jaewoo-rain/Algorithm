gun = 10
def chekPoint(soliders):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soliders
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총 : {0}".format(gun))
chekPoint(2)
print("[함수 밖] 남은 총: {0}".format(gun))

def std_weight(height, gender):
    if gender == "남자":
        weight = round((height*0.01)*(height*0.01)*22,2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height,weight))
    elif gender == "여자":
        weight (height*0.1)*(height*0.1)*21
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height,weight))
    else:
        print("성별을 다시 입력해주세요")

std_weight(175, "남자")