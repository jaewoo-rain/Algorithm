# 세트 (set) 집합
# 중복 안돼, 순서 없음

# 사전은 key와 value, 
# 세트는 값만 존재
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# 여러개 추가
python.update(["1번", "2번"])
print(python)

# 삭제
python.remove("1번")
print(python)