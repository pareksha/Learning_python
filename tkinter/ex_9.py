from tkinter import *

class window:
    def __init__(self,master):
        self.frame1 = Frame(master,width = 200,height = 100)
        self.frame1.pack()

        self.frame2 = Frame(master,width = 200,height = 100)
        self.frame2.pack()

        self.btn_frame1 = Button(self.frame1,text = "Frame 1 button")
        self.btn_frame1.bind("<Button-1>",self.print_frame1)
        self.btn_frame1.pack()

        self.btn_frame2 = Button(self.frame2,text = "Frame 2 button")
        self.btn_frame2.bind("<Button-1>",self.print_frame2)
        self.btn_frame2.pack()

    def print_frame1(self,event):
        print("This is frame 1")

    def print_frame2(self,event):
        print("This is frame 2")


root = Tk()
my_window = window(root)
root.mainloop()
