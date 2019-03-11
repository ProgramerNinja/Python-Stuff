#Jared M.
#Gui-Calculator
#3/7/2019

from tkinter import *


class Application(Frame):
    """ GUI calculator"""
    def __init__(self, master):
        """initilize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Creating buttons for adding subtracting etc"""

        """display"""
        self.entered = Text(self, width=10, height=2, wrap=WORD)
        self.entered.grid(row=0, column=0, columnspan=10, sticky=W)






        """numbers"""
        self.bttn0 = Button(self)
        self.bttn0["text"] = "0"
        self.bttn0["command"] = self.add0
        self.bttn0.grid(row=8, column=2)
        self.bttn0["bg"] = "black"
        self.bttn0["fg"] = "red"

        self.bttn1 = Button(self)
        self.bttn1["text"]= "1"
        self.bttn1["command"] = self.add1
        self.bttn1.grid(row=7, column=1)
        self.bttn1["bg"] = "black"
        self.bttn1["fg"] = "red"

        self.bttn2 = Button(self)
        self.bttn2["text"]= "2"
        self.bttn2["command"] = self.add2
        self.bttn2.grid(row=7, column=2)
        self.bttn2["bg"] = "black"
        self.bttn2["fg"] = "red"

        self.bttn3 = Button(self)
        self.bttn3["text"]= "3"
        self.bttn3["command"] = self.add3
        self.bttn3.grid(row=7, column=3)
        self.bttn3["bg"] = "black"
        self.bttn3["fg"] = "red"

        self.bttn4 = Button(self)
        self.bttn4["text"]= "4"
        self.bttn4["command"] = self.add4
        self.bttn4.grid(row=6, column=1)
        self.bttn4["bg"] = "black"
        self.bttn4["fg"] = "red"

        self.bttn5 = Button(self)
        self.bttn5["text"]= "5"
        self.bttn5["command"] = self.add5
        self.bttn5.grid(row=6, column=2)
        self.bttn5["bg"] = "black"
        self.bttn5["fg"] = "red"

        self.bttn6 = Button(self)
        self.bttn6["text"]= "6"
        self.bttn6["command"] = self.add6
        self.bttn6.grid(row=6, column=3)
        self.bttn6["bg"] = "black"
        self.bttn6["fg"] = "red"

        self.bttn7 = Button(self)
        self.bttn7["text"]= "7"
        self.bttn7["command"] = self.add7
        self.bttn7.grid(row=5, column=1)
        self.bttn7["bg"] = "black"
        self.bttn7["fg"] = "red"

        self.bttn8 = Button(self)
        self.bttn8["text"]= "8"
        self.bttn8["command"] = self.add8
        self.bttn8.grid(row=5, column=2)
        self.bttn8["bg"] = "black"
        self.bttn8["fg"] = "red"

        self.bttn9 = Button(self)
        self.bttn9["text"]= "9"
        self.bttn9["command"] = self.add9
        self.bttn9.grid(row=5, column=3)
        self.bttn9["bg"] = "black"
        self.bttn9["fg"] = "red"


        """Opertators"""
        self.bttnadd = Button(self)
        self.bttnadd["text"]= "+"
        self.bttnadd["command"] = self.add
        self.bttnadd.grid(row=4, column=5)
        self.bttnadd["bg"] = "black"
        self.bttnadd["fg"] = "red"

        self.bttnsub = Button(self)
        self.bttnsub["text"]= "-"
        self.bttnsub["command"] = self.sub
        self.bttnsub.grid(row=5, column=5)
        self.bttnsub["bg"] = "black"
        self.bttnsub["fg"] = "red"

        self.bttntms = Button(self)
        self.bttntms["text"]= "*"
        self.bttntms["command"] = self.tms
        self.bttntms.grid(row=6, column=5)
        self.bttntms["bg"] = "black"
        self.bttntms["fg"] = "red"

        self.bttndiv = Button(self)
        self.bttndiv["text"]= "/"
        self.bttndiv["command"] = self.div
        self.bttndiv.grid(row=7, column=5)
        self.bttndiv["bg"] = "black"
        self.bttndiv["fg"] = "red"

        self.bttneql = Button(self)
        self.bttneql["text"] = "="
        self.bttneql["command"] = self.equate
        self.bttneql.grid(row=8, column=5)
        self.bttneql["bg"] = "black"
        self.bttneql["fg"] = "red"



    """number adding"""
    def add1(self):
        pass

    def add2(self):
        pass

    def add3(self):
        pass

    def add4(self):
        pass

    def add5(self):
        pass

    def add6(self):
        pass

    def add7(self):
        pass

    def add8(self):
        pass

    def add9(self):
        pass

    def add0(self):
        pass

    """Operating"""
    def add(self):
        pass

    def sub(self):
        pass

    def tms(self):
        pass

    def div(self):
        pass

    def equate(self):
        pass





root =Tk()
root.title("Calculator")
root.geometry("150x165")
root["bg"] = "white"
app = Application(root)

root.mainloop()
