import random

from tkinter import *
w = h = 600
x_current = y_current = x_prev = y_prev = 0


def print_dot():
    global x_current, y_current, x_prev, y_prev
    point = random.randint(0, 100)
    if point < 1:
        a, b, c, d, e, f = 0, 0, 0, 0.16, 0, 0
    elif 1 <= point <= 85:
        a, b, c, d, e, f = 0.85, 0.04, -0.04, 0.85, 0, 1.6
    elif 85 < point <= 93:
        a, b, c, d, e, f = 0.2, -0.26, 0.23, 0.22, 0, 1.6
    elif 93 < point <= 100:
        a, b, c, d, e, f = -0.15, 0.28, 0.26, 0.24, 0, 0.44
    else:
        print("Такого не бывает", point)
    x_current = (a * x_prev) + (b * y_prev) + e
    y_current = (c * x_prev) + (d * y_prev) + f
    x_prev = x_current
    y_prev = y_current
    cvs.create_oval(40*(x_current+10), 40*(11-y_current), 40*(x_current+10), 40*(11-y_current), width=1, outline='green')

    root.after(1, print_dot)


root = Tk()

cvs = Canvas(root, width=w, height=h, bg='white')
cvs.pack()

print_dot()

root.mainloop()
