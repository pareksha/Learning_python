from tkinter import *

root = Tk()

def print_hello():
    print("Hello")

def print_chutku():
    print("Chutku")

def print_bhaiya():
    print("Bhiiiiyyyyaaaaa")

my_menu = Menu(root)
root.config(menu = my_menu)

Drop_down_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = Drop_down_menu)
Drop_down_menu.add_command(label = "New", command = print_hello)
Drop_down_menu.add_command(label = "Save", command = print_hello)
Drop_down_menu.add_separator()
Drop_down_menu.add_command(label = "Exit", command = root.quit)


Another_drop_down = Menu(my_menu)
my_menu.add_cascade(label = "Siblings",menu = Another_drop_down)
Another_drop_down.add_command(label = "123",command = print_chutku)
Another_drop_down.add_command(label = "456",command = print_bhaiya)

root.mainloop()
