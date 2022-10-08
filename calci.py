from math import *
from tkinter import *
root = Tk()
root.title("Calculator")
e = Entry(root, width=80, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#defining buttons
def button_click(number):
    global current
    current = e.get()
    e.delete(0, END)
    global str1
    str1 = str(current)+str(number)
    e.insert(0, str1)

def back_space(e):
    input_len = len(e.get())
    e.delete(input_len - 1)
    
def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math="add"
    f_num=float(first_number)
    e.delete(0, END)
    
def button_sub():
    first_number = e.get()
    global f_num
    global math
    math="sub"
    f_num=float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math="multiply"
    f_num=float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math="divide"
    f_num=float(first_number)
    e.delete(0, END)

def button_square():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math="square"
    f_num=float(first_number)
    str1 = str(first_number)+"**2"
    e.insert(0, str1)

def button_power():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math="power"
    f_num=float(first_number)
    str1 = str(first_number)+"**"
    e.insert(0, str1)

def button_10x():
    first_number = e.get()
    global f_num
    global math
    math="10x"
    f_num=float(first_number)
    e.delete(0, END)

def button_sqrt():
    e.insert(0, "sqrt(")
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math="sqrt"
    f_num=float(first_number)
    str1 = "sqrt("+str(first_number)
    e.insert(0, str1)

def button_sin():
    e.insert(0, "sin(")
    first_num = e.get()
    global f_num
    global math
    math="sin"
    f_num = float(first_num)
    e.delete(0, END)
    str1 = "sin(" + str(first_num)
    e.insert(0, str1)

def button_equal():
    if math=="add":
        s_num = e.get()
        e.delete(0, END)
        e.insert(0, float(f_num) + float(s_num))
    if math=="sub":
        s_num = e.get()
        e.delete(0, END)
        e.insert(0, float(f_num) - float(s_num))
    if math=="multiply":
        s_num = e.get()
        e.delete(0, END)
        e.insert(0, float(f_num) * float(s_num))
    if math=="divide":
        s_num = e.get()
        e.delete(0, END)
        e.insert(0, float(f_num) / float(s_num))
    if math=="power":
        s_num = e.get()
        e.delete(0, END)
        e.insert(0, float(f_num)**float(s_num))
    if math=="10x":
        s_num = e.get()
        e.delete(0, END)
        e.insert(0, float(f_num)*(10**float(s_num)))
    if math=="sin":
        e.delete(0, END)
        e.insert(0, sin(f_num))
    if math=="sqrt":
        e.delete(0, END)
        e.insert(0, sqrt(f_num))
    if math=="square":
        e.delete(0, END)
        e.insert(0, f_num**2)



#adding buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_sub)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=40, pady=20, command=button_clear)
button_backspace = Button(root, text="<--", padx=40, pady=20, command=lambda: back_space(e))
button_square = Button(root, text="x^2", padx=40, pady=20, command=button_square)
button_power = Button(root, text="x^y", padx=40, pady=20, command=button_power)
button_sqrt = Button(root, text="sqrt", padx=40, pady=20, command=button_sqrt)
button_10x = Button(root, text="*10^x", padx=40, pady=20, command=button_10x)
#arranging buttons
button_1.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=0)

button_4.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=0)

button_7.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=0)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1 )
button_subtract.grid(row=4, column=2)

button_multiply.grid(row=1, column=3)
button_divide.grid(row=2, column=3)
button_equal.grid(row=3, column=3)
button_square.grid(row=4,column=3)

button_power.grid(row=6, column=0)
button_10x.grid(row=6, column=1)
button_clear.grid(row=6, column=2)
button_backspace.grid(row=6, column=3)

button_sqrt.grid(row=7, column=0, columnspan=1)

root.mainloop()




