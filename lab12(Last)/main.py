from tkinter import *
import numpy as np


def processVector():
    e3.delete(0, 'end')

    a, b = strToVector(e1.get(), e2.get())

    result_matrix = productMatrix(a, b)
    e3.insert(0, result_matrix)


def processMatrix():
    e6.delete(0, 'end')

    result_matrix = productMatrix(e4.get(), e5.get())
    e6.insert(0, result_matrix)


def productMatrix(a, b):
    
    answer = np.array(a).dot(np.array(b))
    return answer


def strToVector(a, b):
    a = a.split()
    b = b.split()

    print(a)
    print(b)

    for i in range(0, len(a)):
        a[i] = int(a[i])

    for i in range(0, len(b)):
        b[i] = int(b[i])

    a_matrix = np.array(a)
    b_matrix = np.array(b)

    print(a_matrix)
    print(b_matrix)

    return a_matrix, b_matrix


def strToMatrix(a, b):
    a = np.array(a)
    b = np.array(b)

    return a, b


window = Tk()

explanation_vec = Label(window, text="벡터 곱 계산기")
vectorA = Label(window, text="A벡터")
vectorB = Label(window, text="B벡터")
result_vec = Label(window, text="결과")

explanation_vec.grid(row=0, column=1)
vectorA.grid(row=1, column=0)
vectorB.grid(row=2, column=0)
result_vec.grid(row=3, column=0)

e1 = Entry(window, bg="yellow")
e2 = Entry(window, bg="yellow")
e3 = Entry(window, bg="yellow")

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

b1 = Button(window, text="계산", command=processVector)
b1.grid(row=4, column=1)

explanation_mtx = Label(window, text="행렬 곱 계산기, 행렬은 [[2,3],[3,4]]의 형태로 입력")
matrixA = Label(window, text="A벡터")
matrixB = Label(window, text="B벡터")
result_mtx = Label(window, text="결과")

explanation_mtx.grid(row=5, column=1)
matrixA.grid(row=6, column=0)
matrixB.grid(row=7, column=0)
result_mtx.grid(row=8, column=0)

e4 = Entry(window, bg="yellow")
e5 = Entry(window, bg="yellow")
e6 = Entry(window, bg="yellow")

e4.grid(row=6, column=1)
e5.grid(row=7, column=1)
e6.grid(row=8, column=1)

b2 = Button(window, text="계산", command=processMatrix)
b2.grid(row=9, column=1)

window.mainloop()

# 이부분 추가 하고부터 안됨 문재가 뭘까?
