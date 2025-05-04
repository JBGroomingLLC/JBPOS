from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Point-of-Sale Application Test").grid(column=0, row=0)
ttk.Button(frm, text="Start Transaction").grid(column=0,row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=1)
root.mainloop()