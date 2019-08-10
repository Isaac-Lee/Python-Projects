def Data():
    d_list = []
    while True:
        d = input('숫자를 입력하세요. F를 입력하면 중지')
        if d=='F':
            break
        d_list.append(int(d))
    return d_list


def Sort(_data, n):
    if n <= 0:
        pass
    else:
        for i in range(n-1):
            if _data[i] > _data[i + 1]:
                x = _data[i]
                _data[i] = _data[i + 1]
                _data[i + 1] = x
        _data = Sort(_data, n-1)
    return _data

data = Data()
print('입력받은 값:',data)
print('정렬 결과:',Sort(data, len(data)))
