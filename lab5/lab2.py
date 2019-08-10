'''
정수를 입력받아 펙토리얼을 계산하는 프로그램을 만들어보자
'''
n = int(input("정수를 입력하시오: "))
nPac = 1
if n == 0:
    print(1)
elif n < 0:
    print("값이 없습니다")
else:
    for i in range(1,n+1):
        nPac *= i
    print("{0}! = {1}".format(n, nPac))