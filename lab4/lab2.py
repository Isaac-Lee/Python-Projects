hight = int(input("높이를 입력하시오: "))
length = 1
n = 0
for i in range(hight):
    print(" "*((hight-1)-n)+"*"*length)
    length += 2
    n += 1
for n in range(3):
    print(" "*(hight-2) + "***")
