#Jared M.
#Gui-movie picker
#3/7/2019

from tkinter import *


class Application(Frame):
    """ GUI Movie Picker"""
    def __init__(self, master):
        """initilize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Creating buttons for adding subtracting etc"""

        Label(self, text="Choose your favorite movie types!").grid(row=1, column=0, sticky=W)

        # self.likes_comedy = BooleanVar()
        # Checkbutton(self,
        #             text="Comedy",
        #             variable = self.likes_comedy,
        #             command = self.update_text).grid(row = 2, column = 0, sticky = W)
        #
        # self.likes_drama = BooleanVar()
        # Checkbutton(self,
        #             text="Drama",
        #             variable=self.likes_drama,
        #             command=self.update_text).grid(row=3, column=0, sticky=W)
        #
        # self.likes_romance = BooleanVar()
        # Checkbutton(self,
        #             text="Romance",
        #             variable=self.likes_romance,
        #             command=self.update_text).grid(row=4, column=0, sticky=W)
        #
        # self.likes_none = BooleanVar()
        # Checkbutton(self,
        #             text="NoNe",
        #             variable=self.likes_none,
        #             command=self.update_text).grid(row=5, column=0, sticky=W)

        self.favorite = StringVar()
        self.favorite.set(None)


        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favorite,
                    value = "comedy.",
                    command = self.update_text(),
                    ).grid(row = 2, column = 0, sticky = W)

        Radiobutton(self,
                    text="Action",
                    variable=self.favorite,
                    value="action.",
                    command=self.update_text,
                    ).grid(row=3, column=0, sticky=W)

        Radiobutton(self,
                    text="Comedic Action",
                    variable=self.favorite,
                    value="comedic action.",
                    command=self.update_text,
                    ).grid(row=4, column=0, sticky=W)


        self.results_txt = Text(self, width=50, height=7, wrap=WORD)
        self.results_txt.grid(row=6, column=0, columnspan=2, sticky=W)

    def update_text(self):
        """Update text widget and user's favorite movie types."""



        message = "your favorite type of movie is "
        message += self.favorite.get()
        self.results_txt.delete(0.0,END)
        self.results_txt.insert(0.0,message)















root =Tk()
root.title("Movie Picker")
root.geometry("225x250")
root["bg"] = "white"
app = Application(root)

root.mainloop()

input()
