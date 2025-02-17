print("Python", "Java", sep = " vs ") # Python vs Java

import sys
print("Python", "Java", file=sys.stdout) # 출력
print("Python", "Java", file=sys.stderr) # 에러

scores = {"수학":0, "영어":50,"코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8),str(score).rjust(4),sep=":")

for num in range(1,21):
    print("대기번호: " + str(num).zfill(3)) # 3자리에서 빈자리는 0으로 채우기

answer = input("아무 값이나 입력하세요 : ") # 항상 String 포멧
print("입력하신 값은" + answer + "입니다")
