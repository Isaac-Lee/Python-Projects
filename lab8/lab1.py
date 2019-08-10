eng_to_kor = {"one": "하나", "two": "둘", "three": "셋", "four": "넷"}

eng_string = input("영어 문장을 입력하세요: ")

eng_list = eng_string.split()

kor_string = ""

kor_list = []

for word in eng_list:
    if word in eng_to_kor:
        kor_list.append(eng_to_kor[word])
        continue
    else:
        kor_list.append(word)
        continue

for word in kor_list:
    kor_string += word+" "

print(kor_string)