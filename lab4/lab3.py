numList = []
for i in range(1,31):
    numList.append(i)
# 리스트 복사
evenNum = numList[:]
oddNum = numList[:]
for n in range(len(numList)):
    if numList[n]%2 == 0:  # 짝수이면 훌수리스트에서 그 번호 삭제
        oddNum.remove(numList[n])
    else:  # 홀수이면 짝수리스트에서 그 번호 삭제
        evenNum.remove(numList[n])
print(evenNum)
print(oddNum)