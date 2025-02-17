# def profile(name, age, lang1, lang2, lang3, lang4):
#     print("이름: {0}\t 나이: {1}".format(name,age))
#     print(lang1,lang2,lang3,lang4)

def profile(name, age, *language):
    print("이름: {0}\t 나이: {1}".format(name,age))
    for lang in language:
        print(lang, end="")
    print()

profile("유재석", 20 ,"자바","파이썬","코틀린")
profile("김태호",21 ,"파이썬")