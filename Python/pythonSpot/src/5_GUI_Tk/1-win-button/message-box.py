import tkinter
from tkinter import messagebox

#messagebox.showinfo("Title", "a Tk MessageBox")
#messagebox.showerror("Error","No disk space left on device")

result = messagebox.askyesno("Python","Would you like to save the data?")
print(result)