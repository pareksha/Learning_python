import tkinter

root = tkinter.Tk()

top_frame = tkinter.Frame(root)
top_frame.pack()

bottom_frame = tkinter.Frame(root)
bottom_frame.pack(side = tkinter.BOTTOM)

button1 = tkinter.Button(top_frame,text = "btn1",bg = 'yellow')
button3 = tkinter.Button(top_frame,text = "btn3",bg = "blue")
button2 = tkinter.Button(bottom_frame,text = "btn2",bg = 'red')

button1.pack(side = tkinter.LEFT)
button2.pack()
button3.pack()

root.mainloop()
