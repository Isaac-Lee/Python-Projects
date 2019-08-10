coin = int(input("투입한 돈: "))
coast = int(input("물건값: "))
change = coin-coast
coin500 = change//500
coin100 = int((change%500)/100)
print("거스름돈:", change)
print("500원 동전의 개수:", coin500)
print("100원 동전의 개수:", coin100)