from tkinter import *

root = Tk()
Label1 = Label(root,text = "Hello",bg = "green")
Label2 = Label(root,text = "World",bg = "yellow")

Label1.pack(side = LEFT,fill = BOTH,expand = True) #fill = X fills horizontally
Label2.pack(fill = BOTH, expand = True) #fill = Y fills vertically

root.mainloop()
