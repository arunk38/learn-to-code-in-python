from tkinter import *


def donothing():
    x = 0

root = Tk()

menubar = Menu(root)

filename = Menu(menubar, tearoff=0)

filename.add_command(label="New", command=donothing)
filename.add_command(label="Open", command=donothing)
filename.add_command(label="Save", command=donothing)
filename.add_separator()
filename.add_command(label="Exit", command=donothing)
menubar.add_cascade(label="File", menu=filename)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()