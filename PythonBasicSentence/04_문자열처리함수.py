python = "Python is Amazing"
print(python.lower) # 모두 소문자로
print(python.upper) # 모두 대문자
print(python[0].isupper) # 첫문자가 대문자인가?
print(len(python)) # 문자길이
print(python.replace("Python", "Java")) # 교체

index = python.index("n") # 첫번째 n이 몇번째 있는지
print(index) 

index = python.index("n", index + 1) # 두번째 n.의 위치
print(index) 

print(python.find("n"))
print(python.find("Java")) # 없을경우 -1
# print(python.index("Java")) # 없을경우 오류

print(python.count("n")) # n이 들어있는 갯수
