"""
Tk has several widgets including:

    Label
    EditText
    Images
    Buttons (Discussed before)
"""

from tkinter import *

root = Tk()
root.minsize(400,100)
root.geometry("400x100")
root.title('Python Tk Examples @ pythonspot.com')
Label(root, text='Python').pack(pady=20, padx=50)

var = StringVar()
textbox = Entry(root, textvariable=var)
textbox.focus_set()
textbox.pack(pady=10, padx=10)

root.mainloop()