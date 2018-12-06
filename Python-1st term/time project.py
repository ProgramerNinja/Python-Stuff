##jared mcmahon
##9-21-18

import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import datetime

def clock():
    total_seconds = calendar.timegm(time.gmtime())
    calendar.timegm(time.gmtime())

    current_second = total_seconds %60
    
    total_minutes = total_seconds // 60
    
    current_minute = total_minutes % 60

    total_hours = total_minutes // 60

    current_hour = total_hours % 60

    current_hour = current_hour % 24

    current_hour = current_hour - 6


    print(current_hour , ":" , current_minute , ":" , current_second)
    

    if current_hour >=12:
        tag="PM"
    else:
        tag="AM"
    
    timex = str(current_hour) + ":" + str(current_minute) + ":" + str(current_second) + tag
    return timex

def quit(*args):
    root.destroy()
def show_time():
    time = clock()
    txt.set(time)
    root.after(1000, show_time)


root = Tk()
root.attributes("-fullscreen", True)
root.configure(background="black")
root.bind("x", quit)
root.after(1000, show_time)
fnt = font.Font(family='Helvetica', size=250, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
