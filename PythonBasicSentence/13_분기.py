absent = [2,5]
index = 1

for student in range(1,21):
    if student in absent: # 속한다면?
        continue
    print("{0}번 학생 책을 읽어봐".format(student))

# 한줄 for문
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(student) for student in students]
print(students)


from random import *
count = 0
for i in range(1, 51): # 1 ~ 50 사이
    time = randrange(5,51) # 5 ~ 50 사이
    ok = '[ ]'
    if 5 <= time <= 15:
        ok = '[O]'
        count +=1
    print("{0} {1}번째 손님 (소요시간 : {2}분)".format(ok,i, time))
print("총 탑승 승개 : {0} 분".format(count))