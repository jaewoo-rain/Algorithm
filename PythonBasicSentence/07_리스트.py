# 리스트 []

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호")) # 1
# 추가
subway.append("하하") 

# 중간에 추가
subway.insert(1,"정형돈") 
print(subway)

# 뒤에서 빼기
print(subway.pop())
print(subway)

# 같은 이름의 사람
subway.append("유재석")
print(subway.count("유재석"))

# 정렬
num_lst = [5,2,4,3,1]
num_lst.sort()
print(num_lst)

# 뒤집기
num_lst.reverse()
print(num_lst)

# # 모두지우기
# num_lst.clear()
# print(num_lst)

# 리스트 합치기
num_lst.extend(subway)
print(num_lst)