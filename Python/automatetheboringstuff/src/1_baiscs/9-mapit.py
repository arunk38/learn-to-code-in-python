import webbrowser
from tkinter import Tk

r = Tk()

r.withdraw()
address = r.selection_get(selection = "CLIPBOARD")
webbrowser.open("https://www.google.com/maps/place/" + address)