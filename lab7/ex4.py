def Data():
    d_list = []
    while True:
        d = input('숫자를 입력하세요. F를 입력하면 중지')
        if d=='F':
            break
        d_list.append(int(d))
    return d_list

def Sort(data):
    N = len(data)
    for k in range(N-1):
        for i in range(N-k-1):
            if data[i] > data[i + 1]:
                x = data[i]
                data[i] = data[i + 1]
                data[i + 1] = x
    return data

data = Data()
print('입력받은 값:', data)
print(len(data))
print('정렬 결과:', Sort(data))
