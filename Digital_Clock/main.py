from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
root.resizable(0,0)
root.geometry("235x50")
# This line is to fix the timer always top
root.attributes('-topmost', True)

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 30), background ="white", foreground = "black")
label.pack(anchor='center')
time()

mainloop()
