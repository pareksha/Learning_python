from tkinter import *


class window:
    def __init__(self,master):
        self.button = Button(master,text = "Button 1",command = self.print_hello)
        self.button.pack(side = LEFT)

        self.btn = Button(master,text = "Button 2",command = self.print_bye)
        self.btn.pack(side = LEFT)

        self.btn3 = Button(master,text = "Quit", command = master.quit) #if you create a frame and want to quit it, do ---->  frame.quit
        self.btn3.pack()

    def print_hello(self):
        print("Hello")

    def print_bye(self):
        print("Bye")


root = Tk()
my_window = window(root)

root.mainloop()
