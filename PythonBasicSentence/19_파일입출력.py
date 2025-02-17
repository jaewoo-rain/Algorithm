# w = 쓰기 -> 작성시 덮어쓰기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# a = append -> 이어쓰기
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")

# r = 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) # 전체 출력
# score_file.close()

# 한줄씩 읽기 readline
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline())
# score_file.close()

# 몇줄인지 모를 때 while문 이용
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 몇줄인지 모를 때 list이용 readlines
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 내용을 읽어와 list형태로 저장됨
for line in lines:
    print(line, end="")
score_file.close()