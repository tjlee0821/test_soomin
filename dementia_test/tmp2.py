from tkinter import ttk
from tkmacosx import Button
def demoColorChange(): button1.confiture(bg="red", fg="yellow")
parent = ttk.Tk()
parent.geometry('500x500')
button1 = ttk.Button(parent, text = 'click me!', command=demoColorChange)    
button1.pack()
parent.mainloop()