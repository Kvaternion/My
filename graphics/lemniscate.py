from math import tan, pi
from tkinter import *
w = h = 600

#TODO: Как-то кривовато вышло, надо будет причесать

alfa = 0#-pi/2
def print_dot():
    global alfa
    x = 2 * r / (tan(alfa) ** 2 + 1)
    y = x * tan(alfa)
    tgb = x*tan(alfa) / (x + z)
    tgb2 = tgb**2
    d = (2*z*tgb2 - 2*r)**2 - 4*(1 + tgb2) * (z**2) * tgb2
    x_0   = (2 * r - 2 * z * tgb2 + d ** 0.5) / (2 + 2 * tgb2)
    x_0_1 = (2 * r - 2 * z * tgb2 - d ** 0.5) / (2 + 2 * tgb2)
    y_0 = (z + x_0) * tgb
    y_0_1 = (z + x_0_1) * tgb
    # print(f"x = {x_0}, y = {y_0} d = {d}, tg2 = {tgb}")
    # cvs.create_oval(300 + z + x, 300 - y, 300 + z + x, 300 - y, width=3, outline='green')
    # cvs.create_oval(300 + z + x_0, 300 - y_0, 300 + z + x_0, 300 - y_0, width=3, outline='blue')
    cvs.create_oval(300 + x -x_0, 300 - (y - y_0), 300 + x - x_0, 300 - (y - y_0), width=2,  outline='orange') # лемниската
    cvs.create_oval(300 + x - x_0_1, 300 - (y - y_0_1), 300 + x - x_0_1, 300 - (y - y_0_1), width=2,
                    outline='orange')  # лемниската (зеркальная часть)
    # cvs.create_line(300, 300, 300 + z + x_0, 300 - y_0)
    # cvs.create_line(300, 300, 300 + z + x, 300 - y)

    alfa += 0.01

    root.after(1, print_dot)


root = Tk()

cvs = Canvas(root, width=w, height=h, bg='white')
cvs.create_line(0, 300, 600, 300)
cvs.create_line(300, 0, 300, 600)
c = 150
r = c/(2**0.5)
z = 50
# cvs.create_oval(350, 300 + r, 350 + 2*r, 300 - r, width=1, outline='red') # окружность
# cvs.create_oval(300, 300, 350, 300, width=4, outline='green')
# cvs.create_oval(350, 300, 350, 300, width=4, outline='green')
# cvs.create_oval(350+2*r, 300, 350+2*r, 300, width=4, outline='green')


# while alfa < pi/2:
#
#     x = 2 * r / (tan(alfa) ** 2 + 1)
#     y = 300 - x * tan(alfa)
#     cvs.create_oval(350 + x, y, 350 + x, y, width=3, outline='blue')
#     alfa += 0.1

cvs.pack()

print_dot()

root.mainloop()
