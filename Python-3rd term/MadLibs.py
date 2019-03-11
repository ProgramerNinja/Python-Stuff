#Jared M.
#Gui-MadLibs
#3/7/2019

from tkinter import *


class Application(Frame):
    """ GUI MadLibs"""
    def __init__(self, master):
        """initilize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Creating buttons for adding subtracting etc"""
        Label(self, text="MadLibs").grid(row=0, column=0, sticky=W)

        Label(self, text="").grid(row=1, column=0, sticky=W)
        Label(self, text="").grid(row=2, column=0, sticky=W)
        Label(self, text="").grid(row=3, column=0, sticky=W)


        self.first_ent = Entry(self)
        self.first_ent.grid(row=1, column=1, columnspan = 3, sticky=W)

        self.second_ent = Entry(self)
        self.second_ent.grid(row=2, column=1, columnspan = 3, sticky=W)

        self.third_ent = Entry(self)
        self.third_ent.grid(row=3, column=1, columnspan = 3, sticky=W)

        Label(self, text="").grid(row=4, column=0, sticky=W)
        Label(self, text="").grid(row=5, column=0, sticky=W)

        self.box1 = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable = self.box1).grid(row = 4, column =1 , sticky = W)
        self.box2 = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.box2).grid(row=4, column=2, sticky=W)
        self.box3 = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.box3).grid(row=4, column=3, sticky=W)

        self.radios = StringVar()
        self.radios.set(None)

        Radiobutton(self,
                    text="",
                    variable=self.radios,
                    value="",
                    ).grid(row=5, column=1, sticky=W)
        Radiobutton(self,
                    text="",
                    variable=self.radios,
                    value="",
                    ).grid(row=5, column=2, sticky=W)
        Radiobutton(self,
                    text="",
                    variable=self.radios,
                    value="",
                    ).grid(row=5, column=3, sticky=W)

        self.bttn0 = Button(self)
        self.bttn0["text"] = ""
        self.bttn0["command"] = self.story_me
        self.bttn0.grid(row=6, column=0)
        self.bttn0["bg"] = "white"
        self.bttn0["fg"] = "black"

    def story_me(self):
        pass











root =Tk()
root.title("MadLibs")
root.geometry("500x500")
root["bg"] = "white"
app = Application(root)

root.mainloop()