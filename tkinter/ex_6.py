from tkinter import *

root = Tk()

Label1 = Label(root,text = "Name")
Label2 = Label(root,text = "Password")

Label1.grid(row = 0,column = 0,sticky = E)#sticky is for alignment. It takes E,W,N,S as values.
Label2.grid(row = 1,column = 0)

#To take entry from the user
Entry1 = Entry(root)
Entry2 = Entry(root)

Entry1.grid(row = 0,column = 1)
Entry2.grid(row = 1,column = 1)

checkbox = Checkbutton(root,text = 'Save Password for this site')
checkbox.grid(columnspan = 2)

root.mainloop()
