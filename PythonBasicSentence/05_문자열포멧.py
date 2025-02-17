# 방법1
print("나는 %d살입니다" % 20) # %d는 정수
print("나는 %s를 좋아해요" % "파이썬") # %s는 문자열
print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

# 방법2
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파판", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파판", "빨간"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color ="빨간"))

# 방버4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요요")