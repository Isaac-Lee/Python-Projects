from tkinter import *

window = Tk()

number_entry = Entry(window)
result_entry = Entry(window)
op_entry = Entry(window)
number_entry.grid(row=0, column=0, columnspan=4)
result_entry.grid(row=1, column=0, columnspan=4)


def process(str):
    number_entry.delete(0, END)
    number_entry.insert("end", str)


def delete():
    number_entry.delete(0, "end")
    result_entry.delete(0, "end")



def plus():
    temp = result_entry.get()
    if temp == "":
        result_entry.insert(END, number_entry.get())
    else:
        result_entry.delete(0, END)
        result_entry.insert(END, int(temp)+int(number_entry.get()))
    number_entry.delete(0, END)
    op_entry.insert(END, "+")



def min():
    temp = result_entry.get()
    if temp == "":
        result_entry.insert(END, number_entry.get())
    else:
        result_entry.delete(0, END)
        result_entry.insert(END, int(temp)-int(number_entry.get()))
    number_entry.delete(0, END)
    op_entry.insert(END, "-")


def mul():
    temp = result_entry.get()
    if temp == "":
        result_entry.insert(END, number_entry.get())
    else:
        result_entry.delete(0, END)
        result_entry.insert(END, (int(temp) * int(number_entry.get())))
    number_entry.delete(0, END)
    op_entry.insert(END, "*")


def div():
    temp = result_entry.get()
    if temp == "":
        result_entry.insert(END, number_entry.get())
    else:
        result_entry.delete(0, END)
        result_entry.insert(END, int(temp) / int(number_entry.get()))
    number_entry.delete(0, END)
    op_entry.insert(END, "/")


# = 클릭시 결과 출력 힌트
def result():
    temp = result_entry.get()
    # 연산자 변수가 + 일때
    if op_entry.get() == "+":
        result_entry.delete(0, END)
        result_entry.insert(END, int(number_entry.get())+int(temp))
    # 연산자 변수가 - 일때
    elif op_entry.get() == "-":
        result_entry.delete(0, END)
        result_entry.insert(END, int(temp)-int(number_entry.get()))

    # 연산자 변수가 * 일때
    elif op_entry.get() == "*":
        result_entry.delete(0, END)
        result_entry.insert(END, int(temp) * int(number_entry.get()))
         #결과창 숫자 지우기
         #결과창에 * 한 값 넣기

    # 연산자 변수가 / 일때
    elif op_entry.get() == "/":
        result_entry.delete(0, END)
        result_entry.insert(END, int(temp) / int(number_entry.get()))
         #결과창 숫자 지우기
         #결과창에 * 한 값 넣기

    number_entry.delete(0, END)


b1 = Button(window, text="7", command=lambda: process("7"))
b2 = Button(window, text="8", command=lambda: process("8"))
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3 = Button(window, text="9", command=lambda: process("9"))
b4 = Button(window, text="+", command=lambda: plus())
b3.grid(row=2, column=2)
b4.grid(row=2, column=3)
b5 = Button(window, text="4", command=lambda: process("4"))
b6 = Button(window, text="5", command=lambda: process("5"))
b5.grid(row=3, column=0)
b6.grid(row=3, column=1)
b7 = Button(window, text="6", command=lambda: process("6"))
b8 = Button(window, text="-", command=lambda: min())
b7.grid(row=3, column=2)
b8.grid(row=3, column=3)
b9 = Button(window, text="1", command=lambda: process("1"))
b10 = Button(window, text="2", command=lambda: process("2"))
b9.grid(row=4, column=0)
b10.grid(row=4, column=1)
b11 = Button(window, text="3", command=lambda: process("3"))
b12 = Button(window, text="*", command=lambda: mul())
b11.grid(row=4, column=2)
b12.grid(row=4, column=3)
b13 = Button(window, text="C", command=lambda: delete())
b14 = Button(window, text="0")
b13.grid(row=5, column=0)
b14.grid(row=5, column=1)
b15 = Button(window, text="=", command=lambda: result())
b16 = Button(window, text="/", command=lambda: div())
b15.grid(row=5, column=2)
b16.grid(row=5, column=3)

window.mainloop()