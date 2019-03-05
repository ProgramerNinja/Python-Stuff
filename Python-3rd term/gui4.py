#Jared M.
#3/5/2019

from tkinter import *


class Application(Frame):
    def __init__(self, master):
        """initilize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.total_clicks = 0 # number of button clicks
        self.total_value = 0 # Total value of clicks
        self.create_widgets()

    def create_widgets(self):
        """creates button that displays clicks"""

        self.lblTotal_clicks = Label(self)
        self.lblTotal_clicks["text"] = self.total_clicks
        self.lblTotal_clicks.grid()

        self.lblTotal_value = Label(self)
        self.lblTotal_value["text"] = self.total_value
        self.lblTotal_value.grid()



        self.bttnadd = Button(self)
        self.bttnadd["text"]= "+"
        self.bttnadd["command"] = self.add_count
        self.bttnadd.grid()
        self.bttnadd["bg"] = "black"
        self.bttnadd["fg"] = "red"

        self.bttnsub = Button(self)
        self.bttnsub["text"]= "-"
        self.bttnsub["command"] = self.sub_count
        self.bttnsub.grid()
        self.bttnsub["bg"] = "black"
        self.bttnsub["fg"] = "blue"

        self.bttntms = Button(self)
        self.bttntms["text"]= "*"
        self.bttntms["command"] = self.tms_count
        self.bttntms.grid()
        self.bttntms["bg"] = "black"
        self.bttntms["fg"] = "green"

        self.bttndiv = Button(self)
        self.bttndiv["text"]= "/"
        self.bttndiv["command"] = self.div_count
        self.bttndiv.grid()
        self.bttndiv["bg"] = "black"
        self.bttndiv["fg"] = "purple"

    def add_count(self):
        self.total_clicks += 1
        self.total_value += 1
        self.lblTotal_clicks["text"] ="Total Clicks: " + str(self.total_clicks)
        self.lblTotal_value["text"] = "Total Value: " + str(self.total_value)

    def sub_count(self):
        self.total_clicks += 1
        self.total_value -= 1
        self.lblTotal_clicks["text"] ="Total Clicks: " + str(self.total_clicks)
        self.lblTotal_value["text"] = "Total Value: " + str(self.total_value)

    def tms_count(self):
        self.total_clicks += 1
        self.total_value *= 5
        self.lblTotal_clicks["text"] ="Total Clicks: " + str(self.total_clicks)
        self.lblTotal_value["text"] = "Total Value: " + str(self.total_value)

    def div_count(self):
        self.total_clicks += 1
        self.total_value //= 2
        self.lblTotal_clicks["text"] ="Total Clicks: " + str(self.total_clicks)
        self.lblTotal_value["text"] = "Total Value: " + str(self.total_value)



root =Tk()
root.title("Click Counter")
root.geometry("400x100")
app = Application(root)

root.mainloop()
