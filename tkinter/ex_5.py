binding a function to a widget
from tkinter import *

root = Tk()

def statement():
    print("Hello World")

btn = Button(root,text = "This is my button",command = statement)#do not use statement()
btn.pack()

root.mainloop()
