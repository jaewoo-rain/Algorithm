# \n: 줄바꿈
print("백문이 불여일견\n백견이 불여일타?")

# \" \' : 문장 내에서 따옴표
# 저는 "양재우" 입니다.
print("저는 \"양재우\" 입니다")

# \\ : 문장내에서 \
print("C:\\Users\\USER\\Desktop ")

# \r: 커서를 맨 앞으로 이동
print("Red Apple \rPine") # 'Red '사라짐

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

url = "http://google.co.kr"
# url = url[7:]
url = url.replace("http://", "")
index = url.find(".")
new_url = url[:index]
result = f"{new_url[:3]}{len(new_url)}{new_url.count("e")}!"
print(result)