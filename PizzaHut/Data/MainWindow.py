import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

win = tk.Tk()
win.title("Pizza Hut Portal") 

win.iconbitmap(r'pz.ico')

def veg():
    import vegmenu

def nveg():
    import nvegmenu

def modmenu():
    win.quit()
    win.destroy()
    import modmenu

def norder():
    win.quit()
    win.destroy()
    import norder

def ordhst():
    win.quit()
    win.destroy()
    import ordhst

veg = ttk.Button(win, text="Veg Menu", command=veg) 
veg.grid(column=0, row=0)

nveg = ttk.Button(win, text="Non Veg Menu", command=nveg) 
nveg.grid(column=1, row=0)

modmenu = ttk.Button(win, text="Modify Menu", command=modmenu) 
modmenu.grid(column=1, row=1)

norder = ttk.Button(win, text="Place New Order", command=norder) 
norder.grid(column=1, row=2)

ordhst = ttk.Button(win, text="Order History", command=ordhst) 
ordhst.grid(column=1, row=3)

