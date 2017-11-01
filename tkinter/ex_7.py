from tkinter import *
root = Tk()

def right(event):
    print("Clicked Right")

def middle(event):
    print("Clicked Middle")

def left(event):
    print("Clicked Left")

frame = Frame(root,width = 200,height = 100)
frame.bind("<Button-1>",right)
frame.bind("<Button-2>",middle)
frame.bind("<Button-3>",left)
frame.pack()

root.mainloop()
