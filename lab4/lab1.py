name = ["홍길동", "강감찬", "이순신", "권율", "정약용"]
nameScore = []
for i in range(len(name)):
    nameScore.append([name[i]])
    nameScore[i].append(int(input('%s의 점수를 입력하시오: ' % name[i])))
    name[i] = nameScore[i]
print(name)