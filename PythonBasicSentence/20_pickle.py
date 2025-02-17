# pickle =? 데이터를 파일 형태로 저장
import pickle
# # wb = 쓴다, binary형식으로, 인코딩 필요없음
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# # profile에 있는 정보를 profile_file에 저장
# pickle.dump(profile, profile_file)
# profile_file.close()

# 읽기 rb
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file에서 전체 정보 불러오기
print(profile)
profile_file.close()

