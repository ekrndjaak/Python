from tkinter import *
from tkinter import messagebox
root = Tk()

def Callhello():
    msg = messagebox.showinfo("Hello Python!","Hello Python!")

btn = Button(root, text="Push", command=Callhello)
btn.place(x=50, y= 50)

root.mainloop()
