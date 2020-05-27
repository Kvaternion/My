import random

from tkinter import *
w = h = 600
x_current, y_current = 178, 280


def print_dot():
    global x_current, y_current
    point = random.randint(0, 2)

    x_current = 0.5*(x_current + node_x[point])
    y_current = 0.5*(y_current + node_y[point])
    cvs.create_oval(x_current, y_current, x_current, y_current, width=1, outline='red')

    root.after(1, print_dot)


root = Tk()

cvs = Canvas(root, width=w, height=h, bg='white')
cvs.pack()
node_x = (5, 500, 550)
node_y = (10, 550, 20)
for i in range(3):
    cvs.create_oval(node_x[i], node_y[i], node_x[i], node_y[i], width=4, outline='black')

print_dot()

root.mainloop()
