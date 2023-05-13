from tkinter import *
from tkinter import messagebox
root = Tk()

def Callhello():
    msg= messagebox.showinfo("Hello Python!", "HELLO PYTOHN!")

btn = Button(root, text="PUSH!", command=Callhello)
btn.place(x=50,y=50)
btn.pack()

C = Canvas(root, bg="green", height=150, width=150)
C.pack()

root.mainloop()