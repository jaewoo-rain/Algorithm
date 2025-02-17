# key 중복안돼

cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3]) # 유재석
print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # 오류
print(cabinet.get(5)) # None

# 없는값 기본 값 설정정
print(cabinet.get(5,"사용가능"))

# 존재확인
print(3 in cabinet) # True
print(5 in cabinet) # False

# 새 손님
print(cabinet)
cabinet["c-20"] = "조세호"
print(cabinet)
cabinet["c-20"] = "김종국"
print(cabinet)

# 손님 나감
del cabinet[3]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 다 나가
cabinet.clear()
print(cabinet)