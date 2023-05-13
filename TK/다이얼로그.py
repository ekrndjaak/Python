from tkinter import *
root = Tk()

root.title("prgraming") 
root.geometry("400x200") 

lbl = Label(root, text="Name")
lbl.pack()

txt = Entry(root)
txt.pack()

btn = Button(root, text="OK")
btn.pack()

root.mainloop()
