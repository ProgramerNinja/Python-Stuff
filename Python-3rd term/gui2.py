#Jared M.
#3/5/2019

from tkinter import *


class Application(Frame):
    def __init__(self, master):
        """initilize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn1 = Button(self, text="I do nothing")
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="Don't click me!!!")
        self.bttn2.configure(bg="magenta")
        self.bttn2.configure(fg="blue")

        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here!"
        self.bttn3["bg"] = "red"
        self.bttn3["fg"] = "orange"









root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")
app = Application(root)

root.mainloop()

