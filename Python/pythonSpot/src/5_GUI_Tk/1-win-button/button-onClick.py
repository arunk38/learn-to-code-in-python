from tkinter import *

master = Tk ()
master.minsize (300, 100)
master.geometry ("320x100")


def callback ():
    print("Click!!!")


b = Button (master, text = "OK", command = callback)
b.place (x = 20, y = 20)

mainloop ()
