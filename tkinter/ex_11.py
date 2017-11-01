from tkinter import *

root = Tk()

my_menu = Menu(root)
root.config(menu = my_menu)

Drop_down_1 = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = Drop_down_1)
Drop_down_1.add_command(label = "A1")
Drop_down_1.add_command(label = "B1")

Drop_down_2 = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu = Drop_down_2)
Drop_down_2.add_command(label = "A2")
Drop_down_2.add_command(label = "B2")

root.mainloop()
