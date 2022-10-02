import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

win = tk.Tk()
win.title("Pizza Hut Portal") 

win.iconbitmap(r'pz.ico')

def ins():
    win.quit()
    win.destroy()
    import insert

def upd():
    win.quit()
    win.destroy()
    import update

def delete():
    win.quit()
    win.destroy()
    import delete

def back():
    win.quit()
    win.destroy()
    import MainWindow


ins = ttk.Button(win, text="Insert In Menu", command=ins) 
ins.grid(column=0, row=0)

upd = ttk.Button(win, text="Update Menu", command=upd) 
upd.grid(column=0, row=1)

delete = ttk.Button(win, text="Delete From Menu", command=delete) 
delete.grid(column=0, row=2)

back = ttk.Button(win, text="Back", command=back) 
back.grid(column=0, row=3)



