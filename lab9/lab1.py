from tkinter import *


def process():
    e3.delete(0, 'end')
    total_money = float(e1.get()) * float(e2.get())
    e3.insert(0, total_money)


window = Tk()
price = Label(window, text="가격")
amount = Label(window, text="갯수")
total = Label(window, text="총액")

price.grid(row=0, column=0)
amount.grid(row=1, column=0)
total.grid(row=2, column=0)

e1 = Entry(window, bg="yellow")
e2 = Entry(window, bg="yellow")
e3 = Entry(window, bg="yellow")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

b1 = Button(window, text="계산", command=process)
b1.grid(row=3, column=1)
window.mainloop()
