from tkinter import *

root = Tk()
e = Entry(root, width=20)
b = Button(root, text="Преобразовать")
l = Label(root, bg='black', fg='white', width=20)

canvas = Canvas()
canvas.create_line(10,10,30,30)


root.mainloop()