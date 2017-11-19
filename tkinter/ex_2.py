from tkinter import *
root = Tk()

topmost_frame = Frame(root)
topmost_frame.pack()

bottommost_frame = Frame(root)
bottommost_frame.pack(side = BOTTOM)

btn1 = Button(topmost_frame,text ="Button 1",fg = "blue",bg = "yellow")
btn2 = Button(bottommost_frame,text = "Button 2",fg = "purple", bg = "red")
btn3 = Button(topmost_frame,text = "Button 0",fg = 'orange',bg = 'white')

btn3.pack(side = LEFT)
btn1.pack()
btn2.pack()


root.mainloop()
