# import pickle

# # as이용해서 저장 + close로 닫을필요 없음
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# # with 이용하여 작성하기
# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# # with 이용하여 불러오기
# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())

# 자동화 퀴즈
content = '''{0} 주차 주간 보고
부서 :
이름 :
업무 요약 :
'''
for i in range(1,51):
    with open("{0}주차.txt".format(i), "w", encoding="utf-8") as file:
        file.write(content.format(i))