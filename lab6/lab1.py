# 소수 판별 프로그램
prime_num_list = []
def prime_num_finder(x):
    if (x == 2):
        return x
    elif(x <= 1):
        return False
    else:
        for i in range(2,x):
            if (x%i == 0):
                return False
            else:
                continue
        return x

for n in range(1, 101):
    i = prime_num_finder(n)
    if (i == False):
        continue
    prime_num_list.append(i)

print(prime_num_list)
