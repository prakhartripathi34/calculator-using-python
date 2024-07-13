from tkinter import *
import math

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

def square_root():
    global equation_text

    try:
        total = str(math.sqrt(eval(equation_text)))
        equation_label.set(total)
        equation_text = total
    except:
        equation_label.set("error")
        equation_text = ""

def cube_root():
    global equation_text

    try:
        total = str(eval(equation_text) ** (1/3))
        equation_label.set(total)
        equation_text = total
    except:
        equation_label.set("error")
        equation_text = ""

window = Tk()
window.title("Calculator")
window.geometry("500x600")
# window.config(bg="black")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('AERIAL', 20), bg="black", width=24, height=2, fg='white')
label.pack()

frame = Frame(window, bg="black")
frame.pack()

button_style = {'height': 4, 'width': 9, 'font': 35, 'bg': 'black', 'fg': 'white'}

# First row
button7 = Button(frame, text=7, **button_style, command=lambda: button_press(7))
button7.grid(row=0, column=0)
button8 = Button(frame, text=8, **button_style, command=lambda: button_press(8))
button8.grid(row=0, column=1)
button9 = Button(frame, text=9, **button_style, command=lambda: button_press(9))
button9.grid(row=0, column=2)
divide = Button(frame, text='/', **button_style, command=lambda: button_press('/'))
divide.grid(row=0, column=3)

# Second row
button4 = Button(frame, text=4, **button_style, command=lambda: button_press(4))
button4.grid(row=1, column=0)
button5 = Button(frame, text=5, **button_style, command=lambda: button_press(5))
button5.grid(row=1, column=1)
button6 = Button(frame, text=6, **button_style, command=lambda: button_press(6))
button6.grid(row=1, column=2)
multiply = Button(frame, text='*', **button_style, command=lambda: button_press('*'))
multiply.grid(row=1, column=3)

# Third row
button1 = Button(frame, text=1, **button_style, command=lambda: button_press(1))
button1.grid(row=2, column=0)
button2 = Button(frame, text=2, **button_style, command=lambda: button_press(2))
button2.grid(row=2, column=1)
button3 = Button(frame, text=3, **button_style, command=lambda: button_press(3))
button3.grid(row=2, column=2)
minus = Button(frame, text='-', **button_style, command=lambda: button_press('-'))
minus.grid(row=2, column=3)

# Fourth row
button0 = Button(frame, text=0, **button_style, command=lambda: button_press(0))
button0.grid(row=3, column=0)
decimal = Button(frame, text='.', **button_style, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)
equal = Button(frame, text='=', **button_style, command=equals)
equal.grid(row=3, column=2)
plus = Button(frame, text='+', **button_style, command=lambda: button_press('+'))
plus.grid(row=3, column=3)

# Fifth row
sqrt_button = Button(frame, text='√', **button_style, command=square_root)
sqrt_button.grid(row=4, column=0)
cbrt_button = Button(frame, text='∛', **button_style, command=cube_root)
cbrt_button.grid(row=4, column=1)
clear_button = Button(frame, text='clear', **button_style, command=clear)
clear_button.grid(row=4, column=2, columnspan=2, sticky="nsew")

window.mainloop()
