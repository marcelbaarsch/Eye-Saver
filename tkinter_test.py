from tkinter import *
from tkinter import ttk
import countdown_timer

for i in range(0,10):
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text=str(i)).grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    
root.mainloop()