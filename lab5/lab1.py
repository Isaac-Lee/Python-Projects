"""
입력된 연도가 윤년인지 판단하는 프로그램을 작성하시오.
"""
year = int(input("연도를 입력하시오: "))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):  # 윤년일때
    print("{0}년은 {1}입니다.".format(year, "윤년"))
else:                                                   # 평년일때
    print("{0}년은 {1}입니다.".format(year, "평년"))