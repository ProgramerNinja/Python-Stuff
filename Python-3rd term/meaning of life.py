#Jared M.
#3/5/2019

from tkinter import *


class Application(Frame):
    """ GUI application which can reveal the meaning of longevity"""
    def __init__(self, master):
        """initilize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        #create instruction label
        self.inst_lbl =Label(self, text = "Enter Password for the secret of life.")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        self.inst_lbl["fg"] ="red"
        self.inst_lbl["bg"] = "black"

        #create label for password
        self.pw_lbl = Label(self, text ="Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        self.pw_lbl["fg"] = "red"
        self.pw_lbl["bg"] = "black"

        #add text box
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)


        #Add submit button
        self.submit_bttn = Button(self, text="Submit", command=self.reveal)
        self.submit_bttn.grid(row=2, column=1, sticky=W)

        #add text widget to display text
        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)


    def reveal(self):
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Eat more Veggies"
        else:
            message = "You did don messed up you little bippit. Now you will never now my secret!!!"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)






root =Tk()
root.title("secret of life")
root.geometry("400x100")
root["bg"] = "black"
app = Application(root)

root.mainloop()