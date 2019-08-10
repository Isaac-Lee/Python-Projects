import numpy as np


def productMatrix(A, B):
    an = A.dot(B)
    return an


# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

a = np.array(a)
b = np.array(b)

print("결과 : \n{}".format(productMatrix(a, b)))
