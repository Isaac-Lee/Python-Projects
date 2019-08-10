from tkinter import *
import numpy as np


def processVector():
    e3.delete(0, 'end')

    try:
        a, b = strToVector(e1.get(), e2.get())
    except TypeError:
        pass

    try:
        result_matrix = productMatrix(a, b)
        e3.insert(0, result_matrix)
    except UnboundLocalError:
        pass



def productMatrix(a, b):
    answer = np.array(a).dot(np.array(b))
    return answer


def strToVector(a, b):
    a = a.split()
    b = b.split()

    print(a)
    print(b)

    converting = True

    for i in range(0, len(a)):
        try:
            a[i] = int(a[i])

        except TypeError:
            e3.delete(0, 'end')
            e3.insert(0, "입력값이 잘못되었습니다.")
            converting = False
            break

        except ValueError:
            e3.delete(0, 'end')
            e3.insert(0, "입력값이 잘못되었습니다.")
            converting = False
            break

    for i in range(0, len(b)):
        try:
            b[i] = int(b[i])

        except TypeError:
            e3.delete(0, 'end')
            e3.insert(0, "입력값이 잘못되었습니다.")
            converting = False
            break

        except ValueError:
            e3.delete(0, 'end')
            e3.insert(0, "입력값이 잘못되었습니다.")
            converting = False
            break

    if converting:
        a_matrix = np.array(a)
        b_matrix = np.array(b)

        print(a_matrix)
        print(b_matrix)

        return a_matrix, b_matrix


window = Tk()
window.title("백터 내적 계산기")

explanation_vec = Label(window, text="벡터 내적 계산기")
vectorA = Label(window, text="A벡터", width=10)
vectorB = Label(window, text="B벡터", width=10)
result_vec = Label(window, text="결과", width=10)

explanation_vec.grid(row=0, column=1)
vectorA.grid(row=1, column=0)
vectorB.grid(row=2, column=0)
result_vec.grid(row=3, column=0)

e1 = Entry(window, width= 30, bg="yellow")
e2 = Entry(window, width= 30, bg="yellow")
e3 = Entry(window, width= 30, bg="yellow")

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

b1 = Button(window, text="계산", command=processVector)
b1.grid(row=4, column=1)

window.mainloop()