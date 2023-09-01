from tkinter import *

def add():
    result = float(num1.get()) + float(num2.get())
    label_result.config(text="Resultado: " + str(result))

def subtract():
    result = float(num1.get()) - float(num2.get())
    label_result.config(text="Resultado: " + str(result))

def multiply():
    result = float(num1.get()) * float(num2.get())
    label_result.config(text="Resultado: " + str(result))

def divide():
    result = float(num1.get()) / float(num2.get())
    label_result.config(text="Resultado: " + str(result))


janela = Tk(
    screenName="Calculadora",
    
)
janela.title("Calculadora")
janela.geometry("300x300")
janela.resizable(False, False)

num1 = Entry(janela, width=10)
num1.pack(pady=10)

num2 = Entry(janela, width=10)
num2.pack(pady=10)

btn_add = Button(janela, text="+", width=5, command=add)
btn_add.pack()

btn_subtract = Button(janela, text="-", width=5, command=subtract)
btn_subtract.pack()

btn_multiply = Button(janela, text="*", width=5, command=multiply)
btn_multiply.pack()

btn_divide = Button(janela, text="/", width=5, command=divide)
btn_divide.pack()

label_result = Label(janela, text="Resultado: ")
label_result.pack(pady=10)


btn_clear= Button(janela, text="Limpar", width=5, command=lambda: (label_result.config(text="Resultado: "), num1.delete(0, END), num2.delete(0, END)))
btn_clear.pack()


janela.mainloop()